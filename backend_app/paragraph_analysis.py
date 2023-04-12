import datefinder
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import math
from NERDA.precooked import EN_BERT_ML, EN_ELECTRA_EN
import nltk
from unidecode import unidecode


nltk.download("punkt")

#model_nerda = EN_BERT_ML()
model_nerda = EN_ELECTRA_EN()

# model_nerda.download_network(dir="./ner_models/")

# model_nerda.load_network(file_path="./ner_models/EN_BERT_ML.bin")
model_nerda.load_network(file_path="./ner_models/EN_ELECTRA_EN.bin")
MODEL = SentenceTransformer('all-mpnet-base-v2')
text = "Former Italian Premier Silvio Berlusconi has been hospitalised in intensive care due to a problem related to a previous infection, but was alert and speaking, according to Italy’s foreign minister. The 86-year-old three-time premier was in the ICU at Milan’s San Raffaele hospital, the clinic where he routinely receives care, said Foreign Minister Antonio Tajani, who is also the leader of Berlusconi’s Forza Italia party. Speaking from Brussels, Tajani said Berlusconi was admitted because of an “unresolved problem” related to a previous infection. Berlusconi has had a series of health problems in recent years. In 2020, he contracted COVID-19. He told reporters after being discharged from a 10-day hospital stay then that the disease had been “insidious” and was the most dangerous challenge he had ever faced. He has had a pacemaker for years, underwent heart surgery to replace an aortic valve in 2016 and has overcome prostate cancer. In January 2022 he was admitted for a reported urinary tract infection. Berlusconi, a media mogul-turned-politician, made a shock return to politics in September’s general elections, winning a Senate seat a decade after being banned from holding public office over a tax fraud conviction.  The 2022 election brought a hard-right-led government to power, with Berlusconi’s Forza Italia party a junior member of a government headed by Prime Minister Giorgia Meloni. In January 2022, Berlusconi withdrew his name from consideration to be Italy’s president."


def retrieve_dates(art):
    return list(datefinder.find_dates(art))


def activate_similarities(similarities: np.array, p_size=10) -> np.array:
    """ Function returns list of weighted sums of activated sentence similarities
    Args:
        similarities (numpy array): it should square matrix where each sentence corresponds to another with cosine similarity
        p_size (int): number of sentences are used to calculate weighted sum 
    Returns:
        list: list of weighted sums
    """
    # To create weights for sigmoid function we first have to create space. P_size will determine number of sentences used and the size of weights vector.
    x = np.linspace(-10, 10, p_size)
    # Then we need to apply activation function to the created space
    y = np.vectorize(rev_sigmoid)
    # Because we only apply activation to p_size number of sentences we have to add zeros to neglect the effect of every additional sentence and to match the length ofvector we will multiply
    activation_weights = np.pad(y(x), (0, similarities.shape[0]-p_size))
    # 1. Take each diagonal to the right of the main diagonal
    diagonals = [similarities.diagonal(each)
                 for each in range(0, similarities.shape[0])]
    # 2. Pad each diagonal by zeros at the end. Because each diagonal is different length we should pad it with zeros at the end
    diagonals = [np.pad(each, (0, similarities.shape[0]-len(each)))
                 for each in diagonals]
    # 3. Stack those diagonals into new matrix
    diagonals = np.stack(diagonals)
    # 4. Apply activation weights to each row. Multiply similarities with our activation.
    diagonals = diagonals * activation_weights.reshape(-1, 1)
    # 5. Calculate the weighted sum of activated similarities
    activated_similarities = np.sum(diagonals, axis=0)
    return activated_similarities


def rev_sigmoid(x: float) -> float:
    return (1 / (1 + math.exp(0.5*x)))


def text_with_paragraphs(art):
    text = art.replace('\n', '')
    sentences = text.split('. ')
    embeddings = MODEL.encode(sentences)

    # Create similarities matrix
    similarities = cosine_similarity(embeddings)
    # Let's plot the result we got
    sns.heatmap(similarities, annot=True).set_title(
        'Cosine similarities matrix')

    # Lets apply our function. For long sentences i reccomend to use 10 or more sentences
    activated_similarities = activate_similarities(similarities, p_size=5)

    # lets create empty fig for our plor
    fig, ax = plt.subplots()
    # 6. Find relative minima of our vector. For all local minimas and save them to variable with argrelextrema function
    # order parameter controls how frequent should be splits. I would not reccomend changing this parameter.
    minmimas = argrelextrema(activated_similarities, np.less, order=2)
    # plot the flow of our text with activated similarities
    sns.lineplot(y=activated_similarities, x=range(
        len(activated_similarities)), ax=ax).set_title('Relative minimas')
    # Now lets plot vertical lines in order to see where we created the split
    plt.vlines(x=minmimas, ymin=min(activated_similarities), ymax=max(
        activated_similarities), colors='purple', ls='--', lw=1, label='vline_multiple - full height')

    # Get the length of each sentence
    sentece_length = [len(each) for each in sentences]
    # Determine longest outlier
    long = np.mean(sentece_length) + np.std(sentece_length) * 2
    # Determine shortest outlier
    short = np.mean(sentece_length) - np.std(sentece_length) * 2
    # Shorten long sentences
    text = ''
    for each in sentences:
        if len(each) > long:
            # let's replace all the commas with dots
            comma_splitted = each.replace(',', '.')
        else:
            text += f'{each}. '
    sentences = text.split('. ')
    # Now let's concatenate short ones
    text = ''
    for each in sentences:
        if len(each) < short:
            text += f'{each} '
        else:
            text += f'{each}. '

    # Get the order number of the sentences which are in splitting points
    split_points = [each for each in minmimas[0]]
    # Create empty string
    rep = []
    for num, each in enumerate(sentences):
        if num == 0:
            rep.append(each)
        else:
            # Check if sentence is a minima (splitting point)
            if num in split_points:
                # If it is than add a dot to the end of the sentence and a paragraph before it.
                rep.append(each)
            else:
                # If it is a normal sentence just add a dot to the end and keep adding sentences.
                rep[-1] = rep[-1] + ' ' + each
    return rep


def semantical_analysis(paragraph):
    par_list = paragraph.split('.')
    sentence_list = []
    entity_tags = []
    for i in range(len(par_list)):
        par_list[i] = par_list[i] + '.'
        ner_results = model_nerda.predict_text(par_list[i])
        sentence_list = sentence_list + ner_results[0]
        entity_tags = entity_tags + ner_results[1]
    print((sentence_list, entity_tags))
    return get_entity_list((sentence_list, entity_tags))


def get_entity_list(ner_results):
    entity_list = []
    for i in range(len(ner_results[0])):
        sentence = ner_results[0][i]
        entity_tags = ner_results[1][i]
        j = 0
        n = len(sentence)
        while j < n:
            print(sentence[j])
            if entity_tags[j][0] == 'B':
                entity_tag = entity_tags[j][2:]
                entity = sentence[j]
                while j+1 < n and entity_tags[j+1][0] == 'I':
                    j += 1
                    entity += " " + sentence[j]
                entity_list.append((entity, entity_tag))
            elif entity_tags[j][0] == 'O':
                pass
            else:
                print("Error with the tag :", entity_tags[j])
            j += 1
    return entity_list


def compare(analyzed_par1, analyzed_par2):
    (text_1, dates_1, elements_1) = analyzed_par1
    (text_2, dates_2, elements_2) = analyzed_par2
    total_count = 0
    splitted_elements_1 = []
    splitted_elements_2 = []
    for elt in elements_1:
        l = elt[0].split(' ')
        for e in l:
            splitted_elements_1.append(((unidecode(e)).lower(), elt[1]))
    for elt in elements_2:
        l = elt[0].split(' ')
        for e in l:
            splitted_elements_2.append(((unidecode(e)).lower(), elt[1]))
    splitted_elements_1 = set(splitted_elements_1)
    splitted_elements_2 = set(splitted_elements_2)
    inter = splitted_elements_1.intersection(splitted_elements_2)
    total_count = len(inter)
    print(total_count, len(splitted_elements_1), len(splitted_elements_2))
    return total_count

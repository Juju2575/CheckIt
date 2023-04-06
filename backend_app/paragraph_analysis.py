import datefinder
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import math


def retrieve_dates(art):
    matches = list(datefinder.find_dates(art))

    if len(matches) > 0:
        print(matches)
    else:
        print('no date found')


text = "Former Italian Premier Silvio Berlusconi has been hospitalised in intensive care due to a problem related to a previous infection, but was alert and speaking, according to Italy’s foreign minister. The 86-year-old three-time premier was in the ICU at Milan’s San Raffaele hospital, the clinic where he routinely receives care, said Foreign Minister Antonio Tajani, who is also the leader of Berlusconi’s Forza Italia party. Speaking from Brussels, Tajani said Berlusconi was admitted because of an “unresolved problem” related to a previous infection. Berlusconi has had a series of health problems in recent years. In 2020, he contracted COVID-19. He told reporters after being discharged from a 10-day hospital stay then that the disease had been “insidious” and was the most dangerous challenge he had ever faced. He has had a pacemaker for years, underwent heart surgery to replace an aortic valve in 2016 and has overcome prostate cancer. In January 2022 he was admitted for a reported urinary tract infection. Berlusconi, a media mogul-turned-politician, made a shock return to politics in September’s general elections, winning a Senate seat a decade after being banned from holding public office over a tax fraud conviction.  The 2022 election brought a hard-right-led government to power, with Berlusconi’s Forza Italia party a junior member of a government headed by Prime Minister Giorgia Meloni. In January 2022, Berlusconi withdrew his name from consideration to be Italy’s president."
model = SentenceTransformer('all-mpnet-base-v2')
sentences = text.split('. ')
embeddings = model.encode(sentences)
print(embeddings.shape)

first_sentence = embeddings[0, :]
second_sentence = embeddings[1, :]
third_sentence = embeddings[2, :]
fourth_sentence = embeddings[3, :]
fifth_sentence = embeddings[4, :]

# How similar is second and third sentence
print(
    f'Dot product of second and third sentence is {second_sentence @ third_sentence}')
print(
    f'Dot product of third and fourth sentence is {third_sentence @ fourth_sentence}')
print(
    f'Dot product of fourth and fith sentence is {fourth_sentence @ fifth_sentence}')


# Create similarities matrix
similarities = cosine_similarity(embeddings)
# Let's plot the result we got
sns.heatmap(similarities, annot=True).set_title('Cosine similarities matrix')


def rev_sigmoid(x: float) -> float:
    return (1 / (1 + math.exp(0.5*x)))


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
text = ''
for num, each in enumerate(sentences):
    # Check if sentence is a minima (splitting point)
    if num in split_points:
        # If it is than add a dot to the end of the sentence and a paragraph before it.
        text += f'\n\n {each}. '
    else:
        # If it is a normal sentence just add a dot to the end and keep adding sentences.
        text += f'{each}. '
print(text)

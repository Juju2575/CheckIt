from gensim import models, corpora
from nltk.tokenize import RegexpTokenizer


def get_topics(title, text):
    print("start1")
    # loading model from disk
    model_path = "./lda_model/lda.model"
    lda = models.ldamodel.LdaModel.load(model_path)
    print("start2")
    # Importing a larger list of stopwords
    with open("./lda_model/eng_stopwords_corrected.txt", "r") as f:
        eng_stopwords = f.readlines()
    for i in range(len(eng_stopwords)):
        eng_stopwords[i] = eng_stopwords[i][:-1]
    english_stopset = set(eng_stopwords)

    dict_path = "./lda_model/lda.dict"
    eng_dict_loaded = corpora.Dictionary.load(dict_path)

    article_content = [title + " " + text]

    # Tokenizing words of articles
    tokenizer = RegexpTokenizer(r"(?u)[\b\#a-zA-Z][\w&-_]+\b")
    article_tokens = list(
        map(
            lambda d: [
                token
                for token in tokenizer.tokenize(d.lower())
                if token not in english_stopset
            ],
            article_content,
        )
    )
    article_bow = [eng_dict_loaded.doc2bow(doc) for doc in article_tokens]

    article_main_topics = lda[article_bow]
    sorted_topics = sorted(
        article_main_topics[0], key=lambda t: -t[1]
    )  # On met [0] car il s'agit d'une list avec 1 seul article

    topics_top_words = get_topics_top_words(lda, 5)

    print(topics_top_words[sorted_topics[0][0]])

    return topics_top_words[
        sorted_topics[0][0]
    ]  # the best topic is at index 0, and it's index is the first element of the tuple


def get_topics_top_words(model, max_words):
    all_topics = model.show_topics(-1, max_words * 2, False, False)
    topics = []
    for topic in all_topics:
        min_score_word = float(abs(topic[1][0][1])) / 10.0
        top_positive_words = list(
            map(
                lambda y: y[0].replace("_", " "),
                filter(lambda x: x[1] > min_score_word, topic[1]),
            )
        )[0:max_words]
        topics.append("[" + ", ".join(top_positive_words) + "]")
    return topics


res = get_topics("Trump", "president")
print(res)

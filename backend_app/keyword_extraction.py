import re
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download("stopwords")
nltk.download("wordnet")

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfTransformer 
from sklearn.feature_extraction.text import CountVectorizer

def clean_article(article):

    stop_words = set(stopwords.words("english"))
    #Add custom stop words ??*
    
    # Remove punctuation
    text = re.sub('[^a-zA-Z]', ' ', str(article))
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove tags
    text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)
    
    # Remove special characters and digits
    text=re.sub("(\\d|\\W)+"," ",text)
    
    # Convert to list from string
    text = text.split()
    
    # Stemming
    ps=PorterStemmer()
    
    # Lemmatisation
    lem = WordNetLemmatizer()
    text = [lem.lemmatize(word) for word in text if not word in stop_words] 

    # Removing verbs
    list_of_verbs = []
    pos_tagged_tokens = nltk.pos_tag(text)

    for i in range(len(pos_tagged_tokens)):
        if pos_tagged_tokens[i][1].startswith('V'):
            list_of_verbs.append(pos_tagged_tokens[i][0])

    text = [word for word in text if not word in list_of_verbs]

    text = " ".join(text)
    
    return text 

def create_tfidf(corpus):

    stop_words = set(stopwords.words("english"))
    
    cv=CountVectorizer(max_df=0.8,stop_words=stop_words, max_features=10000, ngram_range=(1,3))
    
    X=cv.fit_transform(corpus)

    tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
    tfidf_transformer.fit(X)

    return cv, tfidf_transformer

def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse= True)


def extract_topn_from_vector(feature_names, sorted_items, topn=25):
    
    # Use only topn items from vector
    sorted_items = sorted_items[:topn]
    score_vals = []
    feature_vals = []
    
    # Word index and corresponding tf-idf score
    for idx, score in sorted_items:
        # Keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])
 
    # Create tuples of feature,score
    # Results = zip(feature_vals,score_vals)
    results= {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]]=score_vals[idx]
    return results


def get_keywords(title, text):

    article_content = title + ". " + text #string

    corpus = [] #A remplacer!!! Comment sauvegarder du tfidf?

    #Text preprocessing
    clean_article_content = clean_article(article_content)

    #TF-IDF
    cv, tfidf_transformer = create_tfidf(corpus)

    # Generate tf-idf for the given document
    tf_idf_vector=tfidf_transformer.transform(cv.transform([clean_article_content]))

    # Sort the tf-idf vectors by descending order of scores
    sorted_items=sort_coo(tf_idf_vector.tocoo())

    # Extract only the top n; n here is 25
    feature_names=cv.get_feature_names()
    keywords=extract_topn_from_vector(feature_names,sorted_items,5)
    
    return keywords
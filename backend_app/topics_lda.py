from gensim import  models
from gensim.test.utils import datapath

def get_topics(title,text):
    #loading model from disk
    model_path = "../backend_app/lda_model/lda.model"
    lda = models.ldamodel.LdaModel.load(model_path)
    return lda[]
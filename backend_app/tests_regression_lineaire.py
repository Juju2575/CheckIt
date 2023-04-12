from euronews_scraping import *
from twitter_scraping import Tweet
import sys

corres_dict = {'euronews': Euronews_Article,
               'monde-diplomatique': Monde_Article,
               'lemonde': Monde_Article,
               'twitter': Tweet}


def show_infos(url):
    try:
        art = Euronews_Article()
        art.url = url
        art.retrieve_info()
        art.topic_analysis()
        print(art.to_paragraph_list())
    except Exception as e:
        print(e)
        print(sys.exc_info())

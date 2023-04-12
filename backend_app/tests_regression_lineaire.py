from euronews_scraping import *
import sys


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

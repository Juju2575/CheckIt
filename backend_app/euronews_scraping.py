import json
from newspaper import Config
from newspaper import Article
from newspaper.utils import BeautifulSoup

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

config = Config()
config.browser_user_agent = USER_AGENT
config.request_timeout = 10

base_url = 'https://fr.euronews.com/2022/12/13/conference-de-soutien-a-lukraine-laide-doit-arriver-en-temps-reel-sur-le-terrain'


def euronews_retrieve_info(url):
    rep = {}

    article = Article(url, config=config)
    article.download()
    article.parse()
    # print(article.title)
    rep['title'] = article.title

    article_meta_data = article.meta_data

    article_summary = [value for (
        key, value) in article_meta_data.items() if key == 'description']
    #print('article summary : ')
    # print(article_summary)
    try:
        rep['summary'] = article_summary[0]
    except:
        rep['summary'] = ''

    soup = BeautifulSoup(article.html, 'html.parser')
    bbc_dictionary = json.loads(
        "".join(soup.find("script", {"type": "application/ld+json"}).contents))

    # print(bbc_dictionary['@graph'])
    try:
        date_published = [bbc_dictionary['@graph'][0]['datePublished']]
    except:
        date_published = [value for (
            key, value) in bbc_dictionary.items() if key == 'datePublished']
    #print('date publication : ')
    # print(date_published)
    try:
        rep['creationDate'] = date_published[0]
    except:
        rep['creationDate'] = ''

    try:
        article_author = [bbc_dictionary['@graph'][0]['author']["name"]]
    except:
        article_author = [value['name']
                          for (key, value) in bbc_dictionary.items() if key == 'author']
    #print('article author : ')
    # print(article_author)
    try:
        rep['author'] = article_author[0]
    except:
        rep['author'] = ''

    # another method to extract the title
    article_title = [value for (
        key, value) in bbc_dictionary.items() if key == 'headline']
    #print('article title : ')
    # print(article_title)
    try:
        rep['title'] = article_title[0]
    except:
        rep['title'] = ''

    try:
        rep['text'] = article.text
    except:
        rep['text'] = ''

    return rep


# print(euronews_retrieve_info(base_url))

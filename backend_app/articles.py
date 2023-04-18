import topics_lda
import topics_bertopic
from GoogleNews import GoogleNews


class Check_It_Article:
    def __init__(self):
        self.title = ''
        self.url = ''
        self.text = ''
        self.google_articles = []
        self.similar_articles = []

    def set_title(self, title):
        self.title = title

    def retrieve_info(self):
        return

    def google_news(self):
        ggnews = GoogleNews()
        if self.title != '':
            ggnews.get_news(self.title)
            self.google_articles = ggnews.results()

    def set_similar_articles(self):
        return

    def standardize_topics(self):

        if type(self.topics) == list:
            rep = "["
            for topic in self.topics:
                rep += topic + ","
            rep = rep[:len(rep)-1]
            rep += "]"
            self.topics = rep

    def topic_analysis(self):
        self.topics = topics_bertopic.get_topic_keywords(self.title, self.text)
        # self.topics = '[International Politics]'
        # self.topics = topics_lda.get_topics(self.title, self.text)
        self.standardize_topics()

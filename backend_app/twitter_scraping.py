import snscrape.modules.twitter as twitterScraper
import articles
import pandas as pd


class Tweet(articles.Check_It_Article):
    example = 'https://twitter.com/esteban7up/status/1633159042712436737'

    def set_id(self):
        self.id = int(self.url.split('/')[5])

    def set_user(self):
        self.user = self.url.split('/')[3]

    def retrieve_info(self):
        query = 'to_complete'

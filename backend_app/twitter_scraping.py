import snscrape.modules.twitter as twitterScraper
import articles
import datetime


class Tweet(articles.Check_It_Article):
    example = 'https://twitter.com/esteban7up/status/1633159042712436737'

    def set_id(self):
        if 'http' in self.url:
            self.id = int(self.url.split('/')[5])
        else:
            self.id = int(self.url.split('/')[3])

    def set_user(self):
        if 'http' in self.url:
            self.user = self.url.split('/')[3]
        else:
            self.user = self.url.split('/')[1]

    def retrieve_info(self):
        self.set_id()
        self.set_user()
        try:
            query = 'since_id:' + str(self.id-1) + \
                ' max_id:' + str(self.id) + ' filter:safe'
            for r in twitterScraper.TwitterSearchScraper(query).get_items():
                self.text = r.rawContent
                self.title = self.user + ' tweeted :'
                self.summary = self.text
                self.author = self.user
                self.creationDate = r.date
        except:
            query = 'since_id:' + str(self.id-1) + \
                ' max_id:' + str(self.id) + ' -filter:safe'
            for r in twitterScraper.TwitterSearchScraper(query).get_items():
                self.text = r.rawContent
                self.title = self.user + ' tweeted :'
                self.summary = self.text
                self.author = self.user
                self.creationDate = r.date


# example_Tweet = Tweet()
# example_Tweet.url = example_Tweet.example
# example_Tweet.set_id()
# example_Tweet.set_user()
# example_Tweet.retrieve_info()

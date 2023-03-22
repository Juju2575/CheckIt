from topics_lda import get_topics


class Check_It_Article:
    def __init__(self):
        self.title = ''
        self.url = ''
        self.text = ''

    def set_title(self, title):
        self.title = title

    def set_website(self):
        if self.url == '':
            return
        websites = ['euronews', 'bbc', 'lemonde']
        for w in websites:
            if w in self.url:
                self.website = w

    def retrieve_info(self):
        return

    def topic_analysis(self):
        self.topics = get_topics(self.title, self.text)

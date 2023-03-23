from bertopic import BERTopic

model = BERTopic.load("bertopic_model/my_BERTopic")

def get_topic_keywords(title, text):
    
    article_content = [title + ". " + text]

    #Prediction
    topic, _ = model.transform(article_content)

    #Getting topic name
    topic_name = model.get_topic_info(topic[0])["Name"][0]
    key_words = topic_name.split('_')

    #Removing the topic ID
    key_words.pop(0)

    return key_words
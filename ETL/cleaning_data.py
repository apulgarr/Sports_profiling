from googletrans import Translator
import string
import re
import nltk
import pandas as pd

def transform_data(data_path):
    data = pd.read_csv(data_path)

    #Droping the repeated rows
    data = data.drop_duplicates(subset="text")

    #Cleaning the text removing emojis of the user name and cleaning the tweet
    data['text'] = data['text'].apply(clean_text)
    data['user_name'] = data['user_name'].apply(remove_emojis)


def remove_emojis(text):
    return text.encode('ascii', 'ignore').decode('ascii')

def clean_text(text):
    #removing emojis, numbers, hashtags, links, etc
    text = remove_emojis(text)
    text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",text).split())
    text = re.sub('[0-9]+', '', text)

    #Tokenization of the text
    text = re.split('\W+', text)
    text = [word.lower() for word in text]

    #Removing stopwords
    stop_words = set(nltk.corpus.stopwords.words('english'))
    text = [word for word in text if word not in stop_words]

    return text


transform_data('tweets_2.csv')

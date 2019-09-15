from googletrans import Translator
import pandas as pd
import string
import re
import nltk
import enchant

def transform_data(data_path):
    data = pd.read_csv(data_path)

    #Droping the repeated rows
    data = data.drop_duplicates(subset="text")

    #Filling the mising values
    data['user_name'] = data['user_name'].fillna("Unknown")

    #Cleaning the text removing emojis of the user name and cleaning the tweet
    data['text'] = data['text'].apply(clean_text)
    data['user_name'] = data['user_name'].apply(remove_emojis)

    #Normalization of the text Stemming and Lammitization
    data['text_stemmed'] = data['text'].apply(stemming)
    data['text_lemmatized'] = data['text'].apply(lemmatizer)

    #Creating the new normalized file
    data.to_csv('tweets_cleaned.csv', encoding='utf-8')


def remove_emojis(text):
    return text.encode('ascii', 'ignore').decode('ascii')


def remove_trash_words(text):
    checker = enchant.Dict("en_US")
    return checker.check(text)


def stemming(text):
    normalizator = nltk.PorterStemmer()
    text = [normalizator.stem(word) for word in text]
    return text


def lemmatizer(text):
    normalizator = nltk.WordNetLemmatizer()
    text = [normalizator.lemmatize(word) for word in text]
    return text


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

    #Removing empty strings
    text = [word for word in text if word]

    #Removing trash words
    checker = enchant.Dict("en_US")
    text = [word for word in text if remove_trash_words(word)]

    return text


def get_info(file_path):
    data = pd.read_csv(file_path)
    print("Missing values")
    print(data.isna().sum())
    print(data.isnull().sum())
    print("Shape")
    print(data.shape)

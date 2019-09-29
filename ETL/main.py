from get_tweets import Tweets
from cleaning_data import transform_data, get_info
import time

def main():
    t = Tweets("GE4iCBIZ5HYdRleDXRzjFMyD6", "Ko9pvWagBFFt6Hw8Vfs3yMSEGmfcL4N9M5g1jloSpwOqPhP5q6", "967916812288561152-tn1uUHdOunWYg8HcynwU1xTcBYvyv69", "Wg5IzILoJhJI9ryZVGu30rBPDoqxR9nA3tIVzfrNyG7gd")

    print("EXTACTING DATA")
    t.extract_data('tweets')
    print("CLEANING DATA")
    transform_data('tweets.csv',  'cleaned_tweets')
    print("INFO")
    get_info('cleaned_tweets.csv')

if __name__ == "__main__":
    main()

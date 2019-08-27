import pandas as pd
import tweepy
import time

class Tweets(object):

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth =  tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)


    def get_limit_access(self):
        return self.api.rate_limit_status()['resources']['search']


    def extract_data(self):
        data = {'id_user': [], 'user_name': [], 'created_at': [], 'followers': [], 'following': [], 'text': []}
        sports = ['soccer', 'american football', 'volleyball', 'chess', 'cycling', 'baseball', 'ice hockey', 'golf', 'table tennis', 'basketball', 'dodgeball', 'rugby', 'handball', 'wrestling', 'water polo', 'skiing', 'badminton', 'field hockey', 'bowling', 'lacrosse', 'boxing', 'cricket']

        for sport in sports:
            word = 'i love %s' % (sport)

            try:
                tweets = tweepy.Cursor(self.api.search, q=word, lang='en',tweet_mode='extended').items(1000)
                print(self.get_limit_access())

                for tweet in tweets:
                    if 'retweeted_status' not in dir(tweet):
                        data['id_user'].append(tweet.id_str)
                        data['user_name'].append(tweet.user.name)
                        data['followers'].append(tweet.user.followers_count)
                        data['following'].append(tweet.user.friends_count)
                        data['created_at'].append(tweet.created_at)
                        data['text'].append(tweet.full_text)
                    else:
                        data['id_user'].append(tweet.retweeted_status.id_str)
                        data['user_name'].append(tweet.retweeted_status.user.screen_name)
                        data['followers'].append(tweet.retweeted_status.user.followers_count)
                        data['following'].append(tweet.retweeted_status.user.friends_count)
                        data['created_at'].append(tweet.retweeted_status.created_at)
                        data['text'].append(tweet.retweeted_status.full_text)

            except tweepy.TweepError:
                print("Waiting for the next time frame")
                time.sleep(15 * 60)

        data_frame = pd.DataFrame(data=data, columns=['id_user', 'user_name', 'created_at', 'followers', 'following', 'text']).to_csv('tweets_2.csv', index=False, encoding='utf-8')


tweet = Tweets(
            'GE4iCBIZ5HYdRleDXRzjFMyD6',
            'Ko9pvWagBFFt6Hw8Vfs3yMSEGmfcL4N9M5g1jloSpwOqPhP5q6',
            '967916812288561152-tn1uUHdOunWYg8HcynwU1xTcBYvyv69',
            'Wg5IzILoJhJI9ryZVGu30rBPDoqxR9nA3tIVzfrNyG7gd'
            )

tweet.extract_data()
#print(tweet.get_limit_access())



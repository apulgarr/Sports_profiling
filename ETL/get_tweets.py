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


    def extract_data(self, out_path):
        data = {'user_name': [], 'likes': [], 'text': [], 'sport': []}
        sports = ['soccer', 'american football', 'volleyball', 'chess', 'cycling', 'baseball', 'ice hockey', 'golf', 'table tennis', 'basketball', 'dodgeball', 'rugby', 'handball', 'wrestling', 'water polo', 'skiing', 'badminton', 'field hockey', 'bowling', 'lacrosse', 'boxing', 'cricket']

        for sport in sports:

            try:
                print(sport)
                tweets = tweepy.Cursor(self.api.search, q=sport, lang='en',tweet_mode='extended').items(1000)
                print(self.get_limit_access())

                for tweet in tweets:
                    if 'retweeted_status' not in dir(tweet):
                        data['user_name'].append(tweet.user.name)
                        data['likes'].append(tweet.favorite_count)
                        data['text'].append(tweet.full_text)
                        data['sport'].append(sport)
                    else:
                        data['user_name'].append(tweet.retweeted_status.user.screen_name)
                        data['likes'].append(tweet.retweeted_status.favorite_count)
                        data['text'].append(tweet.retweeted_status.full_text)
                        data['sport'].append(sport)

            except tweepy.TweepError:
                print("Waiting for the next time frame")
                time.sleep(15 * 60)

        path = "%s.csv" % (out_path) 
        data_frame = pd.DataFrame(data=data, columns=['user_name', 'likes', 'text', 'sport']).to_csv(path, index=False, encoding='utf-8')


if __name__ == "__main__":
    pass

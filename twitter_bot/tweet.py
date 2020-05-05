import tweepy
import time
from nolooking import secret

auth = tweepy.OAuthHandler(secret.twitter_api_key, secret.twitter_api_secret)
auth.set_access_token(secret.twitter_key, secret.twitter_secret)

api = tweepy.API(auth)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(2000)


search_string = 'Jeremiah Wise'
numberOfTweets = 5

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break



#Genrous Bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#
#     print(follower.name)

import tweepy
import secret

auth = tweepy.OAuthHandler('twitter_api_key', 'twitter_api_secret')
auth.set_access_token('twitter_key', 'twitter_secret')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

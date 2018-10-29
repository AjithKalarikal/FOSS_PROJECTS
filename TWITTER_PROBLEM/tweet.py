#importing libraries
import tweepy
from keys import *

#Twitter account Authentication

auth=tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(akey,asecret)

api=tweepy.API(auth)

#Sending the tweet

api.update_status('Hello World')




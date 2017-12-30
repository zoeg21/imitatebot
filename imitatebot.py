#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:49:33 2017
@author: Zoe Gordin

This bot utilizes MarkovBot (https://github.com/esdalmaijer/markovbot) and
get_all_tweets(https://gist.github.com/yanofsky/5436496).
imitatebot uses MarkovBot's markov text analysis to imitate a twitter user
when tweeted at with proper format ("@imitatebot string @handle..") where string can be 
any string and @handle is the handle of the twitter user to imitate.



"""
from twitter import Twitter, OAuth, TwitterStream
import secrets #consumer and access keys
import get_all_tweets
import time
from markovbot import MarkovBot

imitatebot = MarkovBot()

imitatebot.twitter_login(secrets.cons_key, secrets.cons_secret, secrets.access_token, secrets.access_token_secret)
oauth = OAuth(secrets.access_token, secrets.access_token_secret, secrets.cons_key, secrets.cons_secret)
stream = TwitterStream(auth = oauth)
twitter = Twitter(auth=oauth)

 #begins stream filtering through tweets that mention @imitatebot
iterator = stream.statuses.filter(track='@imitatebot')
#each tweet is a json with all tweet information
for tweet in iterator:
    tweeter = tweet['user']['screen_name'] #the twitter user that tweeted at the bot
    text = tweet['text'] #the text of the tweet
    words = text.split(' ') #to get each string in the tweet
    if(words[2][0]!='@'):
        continue
    else:
     handle = words[2] #if the tweet is formatted properly this is the handle to imitate
    #the bot reads in all tweets of the user handle and overwrites previous info
     imitatebot.read(get_all_tweets.get_all_tweets(handle),overwrite=True)
     prefix = '@%s' %tweeter #the bot tweets at whoever tweeted at the bot
     suffix = '#imitatebot imitated %s' %handle 
    #tweets the imitation tweet
     imitatebot.twitter_tweeting_start(days=0, hours=0, minutes=1,keywords=None, prefix=prefix, suffix=suffix)
     time.sleep(60.5)#sleep to give the bot time to tweet
     imitatebot.twitter_tweeting_stop()#stops the bot tweeting after one tweet and waits for the next tweet














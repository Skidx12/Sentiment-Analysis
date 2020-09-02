# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:52:10 2020

@author: Sajal
"""

import os
import tweepy as tw
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import pandas as pd
import csv
import re #regular expression

from textblob import TextBlob
import string
import preprocessor as p
import time
#from preprocessor.api import clean, tokenize, parse


consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONUSMER_SECRET' 
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

#user = api.get_user('goosyboozy')
#print(user)
#api.update_status("Tweeting from python is far better than usual Internet. HAAHHAHAHA!!! #learningsomethingnew")

tweets = []
text_query = ['depressed','hate']
count = 100
try:
# Pulling individual tweets from query
    for tweet in api.search(q=text_query, count=count):
# Adding to list that contains all tweets
      tweets.append((tweet.created_at,tweet.id,tweet.text,tweet.retweet_count))
      # Creation of dataframe from tweets list
      tweetsdf = pd.DataFrame(tweets,columns=['Datetime', 'Tweet Id', 'Text', 'Retweet count'])

      # Converting dataframe to CSV
      tweetsdf.to_csv('{}-tweets.csv'.format(text_query)) 
except BaseException as e:
    print('failed on_status,',str(e))
    time.sleep(3)


"""
#print(api.get_user('goosyboozy'))
#declare file paths as follows for three files
telemedicine_tweets = "data/telemedicine_data_extraction/telemedicine_data.csv"
epilepsy_tweets = "data/telemedicine_data_extraction/epilepsy_data.csv"
heart_stroke_tweets = "data/telemedicine_data_extraction/heart_stroke_tweets_data.csv"

#columns of the csv file
COLS = ['id', 'created_at', 'source', 'original_text','clean_text', 'sentiment','polarity','subjectivity', 'lang',
'favorite_count', 'retweet_count', 'original_author',   'possibly_sensitive', 'hashtags',
'user_mentions', 'place', 'place_coord_boundaries']

#HappyEmoticons
emoticons_happy = set([
    ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3'
    ])


# Sad Emoticons
emoticons_sad = set([
    ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';('
    ])


#Emoji patterns
emoji_pattern = re.compile("["
         u"\U0001F600-\U0001F64F"  # emoticons
         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
         u"\U0001F680-\U0001F6FF"  # transport & map symbols
         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
         u"\U00002702-\U000027B0"
         u"\U000024C2-\U0001F251"
         "]+", flags=re.UNICODE)
#combine sad and happy emoticons
emoticons = emoticons_happy.union(emoticons_sad)

clean_text = p.clean(twitter_text)


def clean_tweets(tweet):
 
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(tweet)
#after tweepy preprocessing the colon symbol left remain after      #removing mentions
    tweet = re.sub(r':', '', tweet)
    tweet = re.sub(r'‚Ä¶', '', tweet)
#replace consecutive non-ASCII characters with a space
    tweet = re.sub(r'[^\x00-\x7F]+',' ', tweet)
#remove emojis from tweet
    tweet = emoji_pattern.sub(r'', tweet)
#filter using NLTK library append it to a string
    filtered_tweet = [w for w in word_tokens if not w in stop_words]
    filtered_tweet = []
#looping through conditions
    for w in word_tokens:
#check tokens against stop words , emoticons and punctuations
        if w not in stop_words and w not in emoticons and w not in string.punctuation:
            filtered_tweet.append(w)
    return ' '.join(filtered_tweet)
    #print(word_tokens)
    #print(filtered_sentence)return tweet


def write_tweets(keyword, file):
    #If the file exists, then read the existing data from the CSV file.
    if os.path.exists(file):
        df = pd.read_csv(file, header=0)
    else:
        df = pd.DataFrame(columns=COLS)
    #page attribute in tweepy.cursor and iteration
    for page in tw.Cursor(api.search, q=keyword,
                              count=200, include_rts=False):
        for status in page:
            new_entry = []
            status = status._json
            if status['lang'] != 'en':
                continue
            if status['created_at'] in df['created_at'].values:
              i = df.loc[df['created_at'] == status['created_at']].index[0]
              if status['favorite_count'] != df.at[i, 'favorite_count'] or \
              status['retweet_count'] != df.at[i, 'retweet_count']:
                  df.at[i, 'favorite_count']= status['favorite_count']
                  df.at[i, 'retweet_count'] = status['retweet_count']
                  continue

filtered_tweet=clean_tweets(clean_text)
"""
"""
auth = tw.OAuthHandler(consumer_key,consumer_secret,callback=None)
#auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

"""

#posting to profile

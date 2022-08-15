"""Imports/Set-Up"""
import tweepy
from creds import bearer_token
client = tweepy.Client(bearer_token=bearer_token)
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
sia = SIA()
# nltk corupus downloads
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')

"""General Resources"""
# how to write better search queries:
# https://github.com/twitterdev/getting-started-with-the-twitter-api-v2-for-academic-research/blob/main/modules/5-how-to-write-search-queries.md
# Building high-quality filters for getting Twitter data
# https://developer.twitter.com/en/docs/tutorials/building-high-quality-filters
# How to use the Twitter API v2 in Python using Tweepy
# https://www.youtube.com/watch?v=0EekpQBEP_8

"""Define Queries"""
keyword = "trump"
query = f"{keyword} -is:retweet" #excludes re-tweets

"""Get Recent Tweets"""
# docs -> https://docs.tweepy.org/en/stable/client.html#tweepy.Client.search_recent_tweets
# get 100 tweets w/ keyword (100 is the maximum # of results per request)
tweets = client.search_recent_tweets(query=query, max_results=100)
# use pagination to get more than 100 tweets (multiple requests will be made)
more_tweets = [tweet for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=1000)]
# use pagination to find all tweets that match keyword (no limit is set, be careful, we are only using essential tier)
all_tweets = [tweet for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten()]

"Get Recent Tweet Counts"
# granularity default is 1 hours
# docs -> https://docs.tweepy.org/en/stable/client.html#tweepy.Client.get_recent_tweets_count
counts = client.get_recent_tweets_count(query=query, granularity="day")

"""Get Polarity Score for Individual Tweet"""
tweet = tweets[0]
text = tweet.text
sentenced = nltk.tokenize.sent_tokenize(text) # tokenizes tweet text by sentence
scores = [sia.polarity_scores(sentence) for sentence in sentenced]

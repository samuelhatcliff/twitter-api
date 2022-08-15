import tweepy
from creds import api_key, api_secret_key, bearer_token, access_token, access_token_secret


# how to write better search queries:
# https://github.com/twitterdev/getting-started-with-the-twitter-api-v2-for-academic-research/blob/main/modules/5-how-to-write-search-queries.md
# Building high-quality filters for getting Twitter data
# https://developer.twitter.com/en/docs/tutorials/building-high-quality-filters
# How to use the Twitter API v2 in Python using Tweepy
# https://www.youtube.com/watch?v=0EekpQBEP_8
keyword = "trump"
query = f"{keyword} -is:retweet"
client = tweepy.Client(bearer_token=bearer_token)


# get 100 tweets w/ keyword (100 is the maximum # of results per request)
tweets = client.search_recent_tweets(query=query, max_results=100)
# use pagination to get more than 100 tweets (multiple requests will be made)
more_tweets = [tweet for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=1000)]
# use pagination to find all tweets that match keyword (no limit is set, be careful, we are only using essential tier)
all_tweets = [tweet for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten()]

counts = client.get_recent_tweets_count(query=query, granularity="day")
# auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
# api = tweepy.API(auth)



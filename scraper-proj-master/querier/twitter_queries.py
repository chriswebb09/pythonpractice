#!/usr/bin/env python3
from .query import BaseQuery
import json
from twitter import Twitter, OAuth, TwitterHTTPError

class TwitterQuery(BaseQuery):
    OAUTH_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    OAUTH_SECRET = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    CONSUMER_KEY = "xxxxxxxxxxxxxxxxxxxx"
    CONSUMER_SECRET = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    def __init__(self, search_term, count=20):
        super(TwitterQuery, self).__init__(search_term)
        self.connection = Twitter(auth=OAuth(self.OAUTH_TOKEN, self.OAUTH_SECRET, self.CONSUMER_KEY, self.CONSUMER_SECRET))
        self.count = count

    def get_results(self):
        tweets = self.connection.search.tweets(q=self.search_term+'+python', result_type='recent', count=self.count, lang="en", max_id=None)
        results = []
        for tweet in tweets['statuses']:
            results.append({'text': tweet['text'], 'user': tweet['username'], 'date': tweet['date']})
        return results

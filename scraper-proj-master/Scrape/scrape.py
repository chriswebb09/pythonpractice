#!/usr/local/env python3
# -*- coding: utf-8

__author__ = 'ChrisWebb'

from bs4 import BeautifulSoup
import requests
import sys

class UserSearch():
    '''Url Search Term Object'''

    def __init__(self, **kwargs):
        self.url = sys.argsv[0]
        self.search_term = sys.argsv[1]
        self.num_results = sys.argsv][2]
        self.search_strength = sys.argsv[3]


    def check_url(self):
            r = requests.get(self.url)
            return r.text


    def __str__(self):
        return "Search term: {} \n{}Search vigor: {}\n Results: {}".format(
            self.search_term, self.search_strength, self.num_results)
        )



def main():
    chris = UserSearch()
    print(chris.__str__)
    print(chris.check_url())


if __name__ == "__main__":
    main()


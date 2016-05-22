#!/usr/bin python

# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup

TAG_RE = re.compile(r'<[^>]+>')


def get_webdata(url):
    r = requests.get(url)
    return r.text


def soupify_data(data):
    soup = BeautifulSoup(data, "html.parser")
    soup_list = soup.findAll(attrs={'class': 'titletext'})
    return soup_list


def remove_tags(text):
    string_text = str(text)
    detagged_string_text = TAG_RE.sub('', string_text)
    new_string_text = re.sub('&\w+;', '', detagged_string_text)
    return new_string_text

if __name__ == "__main__":
    web_data = get_webdata("http://www.news.google.com")
    soup_news = soupify_data(web_data)
    news_items = remove_tags(soup_news)
    news_list = news_items.split(",")
    for item in news_list:
        print(item)

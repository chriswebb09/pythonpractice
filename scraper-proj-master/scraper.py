#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


def scrape_headlines(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    for link in soup.find_all('h2'):
        print(link)

def main():
    scrape = scrape_headlines("http://www.bloomberg.com")

if __name__ == '__main__':
   main()

#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-

import requests


def get_headers(url):
    r = requests.get(url)
    return r.headers


def main():
    url_input = input("Input url: ")
    header = get_headers(url_input)
    print(header)

if __name__ == "__main__":
    main()

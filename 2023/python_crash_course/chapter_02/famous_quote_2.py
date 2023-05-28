#!/usr/bin/env python3
"""
created: 2023/05/27 19:27:28
@author: seraph★776
project: Python Crash Course
metadoc: 2-5. Famous Quote #2
"""
from bs4 import BeautifulSoup
import requests


def get_quotes():
    output = []
    source = requests.get('https://quotes.toscrape.com/')
    soup = BeautifulSoup(source.text, 'lxml')
    all_quotes = soup.find_all('div', attrs={'class': 'quote'})
    for i in all_quotes:
        author = i.find('small', attrs={'class': 'author'}).text
        text = i.find('span', attrs={'class': 'text'}).text
        record = (author, text)
        output.append(record)
    return output


def display_quotes(records: list):
    for item in records:
        person = item[0]
        quote = item[1]
        print(f'{person} once said, {quote}')


if __name__ == '__main__':
    quotes = get_quotes()
    display_quotes(quotes)

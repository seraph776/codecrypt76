#!/usr/bin/env python3
"""
created: 2023/05/28 13:05:27
@author: seraph★776
project: Python Crash Course
metadoc: 3-2. Greetings
"""

from names import names as name_list
import random


def greetings():
    titles = ('mr.', 'mrs.', 'miss', 'madam')
    for name in name_list('data/names.txt'):
        print(f'Hello {random.choice(titles).title()} {name.title()}, would you like to learn Python today?!')


if __name__ == '__main__':
    greetings()

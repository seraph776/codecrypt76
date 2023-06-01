#!/usr/bin/env python3
"""
created: 2023/06/01 17:09:30
@author: seraph★776
project: Python Crash Course
metadoc: 4-13. Buffet
"""


def buffet():
    menu = ('steak', 'rice', 'brocolli', 'salad', 'beer')
    print('We offer the following menu items:')
    for food in menu:
        print(f'- {food}')


if __name__ == '__main__':
    buffet()

#!/usr/bin/env python3
"""
created: 2023/06/02 20:08:33
@author: seraph★776
project: Python Crash Course
metadoc: 5-7. Favorite Fruit
"""


def favorite_fruit(lst):
    fruits = ['blueberries', 'bananas', 'kiwi', 'mango']
    for fruit in lst:
        if fruit in fruits:
            print(f'{fruit} is one of my favorite fruits!')
        else:
            print(f'I do not like {fruit}.')


if __name__ == '__main__':
    fruit_list = ['straw berries', 'blueberries', 'apples', 'mango', 'bananas', 'grapes', 'kiwi', 'lime']
    favorite_fruit(fruit_list)

#!/usr/bin/env python3
"""
created: 2023/05/31 20:50:51
@author: seraph★776
project: Python Crash Course
metadoc: 4-10. Slices
"""


def slices(filename):
    with open(filename) as file_obj:
        toppings = [i.strip() for i in file_obj]
    print(f'The first toppings on the list are: {toppings[:3]}')
    print(f'Three middle items from the list are: {toppings[1:-2]}')
    print(f'The last three items in the list are: {toppings[:-3]}')


if __name__ == '__main__':
    slices('data/toppings.txt')

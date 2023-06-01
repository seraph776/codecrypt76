#!/usr/bin/env python3
"""
created: codecrypt76/05/28 13:17:11
@author: seraph★776
project: Python Crash Course
metadoc: 3-3. Your Own List
"""

import random


def transportation(filename):
    colors = ('red', 'orange', 'black', 'grey', 'blue')
    with open(filename) as file_obj:
        vehicles = [i.strip() for i in file_obj]

    for car in vehicles:
        print(f'I would like to own a {random.choice(colors)} {car} someday.')


if __name__ == '__main__':
    transportation('data/vehicles.txt')

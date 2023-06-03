#!/usr/bin/env python3
"""
created: 2023/06/02 19:18:33
@author: seraph★776
project: Python Crash Course
metadoc: 5-6. Stages of Life
"""


def stages_of_life(age):
    if age < 2:
        return 'baby'
    elif 2 <= age < 4:
        return 'toddler'
    elif 4 <= age < 13:
        return 'kid'
    elif 13 <= age < 20:
        return 'teenager'
    elif 20 <= age < 65:
        return 'adult'
    elif age < 65:
        return 'elder'


if __name__ == '__main__':
    print(stages_of_life(12))

#!/usr/bin/env python3
"""
created: codecrypt76/05/28 09:45:33
@author: seraph★776
project: Python Crash Course
metadoc: 3-1. Names
"""


def names(filename) -> list:
    with open(filename, 'r') as file_obj:
        name_list = [i.strip() for i in file_obj]
    return name_list


if __name__ == '__main__':
    for name in names('data/names.txt'):
        print(name)

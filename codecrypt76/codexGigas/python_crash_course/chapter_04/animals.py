#!/usr/bin/env python3
"""
created: codecrypt76/05/30 13:09:58
@author: seraph★776
project: Python Crash Course
metadoc: 4-2. Animals
"""


def animals():
    with open('data/animals.txt') as fo:
        animal_list = [i.strip() for i in fo]

    return f"The {', '.join(animal_list[:-1])}, and {''.join(animal_list[-1])} are my totems."


if __name__ == '__main__':
    print(animals())

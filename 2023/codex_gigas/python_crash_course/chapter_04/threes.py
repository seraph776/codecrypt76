#!/usr/bin/env python3
"""
created: 2023/05/31 19:51:44
@author: seraph★776
project: Python Crash Course
metadoc: 4-7. Threes
"""


def threes():
    return [n for n in range(1, 31) if n % 3 == 0]


if __name__ == '__main__':
    print(threes())

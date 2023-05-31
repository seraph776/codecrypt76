#!/usr/bin/env python3
"""
created: 2023/05/30 20:38:22
@author: seraph★776
project: Python Crash Course
metadoc: 4-5. Summing a Million
"""


def summing_a_million():
    lst = [n for n in range(1, 1_000_001)]
    return min(lst), max(lst), sum(lst)


if __name__ == '__main__':
    print(summing_a_million())
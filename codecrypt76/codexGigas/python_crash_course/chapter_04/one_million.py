#!/usr/bin/env python3
"""
created: codecrypt76/05/30 20:13:05
@author: seraph★776
project: Python Crash Course
metadoc: 4-4. One Million
"""


def one_million():
    return (n for n in range(1, 1_000_001))


if __name__ == '__main__':
    for n in one_million():
        print(n)

#!/usr/bin/env python3
"""
created: 2023/05/31 22:22:00
@author: seraph★776
project: Codeguppy
metadoc: Calculate the sum of even numbers greater than 10 and less than 30
"""


def solution():
    return sum([n for n in range(100) if n % 2 == 0 and 10 < n < 30])


if __name__ == '__main__':
    print(solution())

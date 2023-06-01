#!/usr/bin/env python3
"""
created: codecrypt76/05/30 15:36:39
@author: seraph★776
project: Codeguppy
metadoc: Print the odd numbers less than 100
"""


def solution():
    return ', '.join([str(n) for n in range(1, 101) if n % 2 == 1])


if __name__ == '__main__':
    print(solution())

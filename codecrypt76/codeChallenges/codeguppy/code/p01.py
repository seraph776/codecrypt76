#!/usr/bin/env python3
"""
created: codecrypt76/05/30 15:32:57
@author: seraph★776
project: Codeguppy
metadoc: Print numbers from 1 to 10
"""


def solution():
    return ', '.join([str(n) for n in range(1, 11)])


if __name__ == '__main__':
    print(solution())
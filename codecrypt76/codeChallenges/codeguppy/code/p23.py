#!/usr/bin/env python3
"""
created: 2023/06/02 18:05:43
@author: seraph★776
project: Codeguppy
metadoc: Reverse a string
"""


def solution(lst):
    return ''.join(list(reversed(lst)))


if __name__ == '__main__':
    print(solution('hello World!'))

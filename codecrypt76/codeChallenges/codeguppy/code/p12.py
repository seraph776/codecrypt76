#!/usr/bin/env python3
"""
created: 2023/06/02 17:57:38
@author: seraph★776
project: Codeguppy
metadoc: Create a function that receives an array of numbers as argument and returns an
array containing only the positive numbers
"""


def solution(lst):
    return list(filter(lambda i: i > 0, lst))


if __name__ == '__main__':
    print(solution([-1, 2, -3, 4, 5, -6, -7, 8, -9]))

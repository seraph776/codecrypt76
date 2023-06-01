#!/usr/bin/env python3
"""
created: 2023/05/31 22:19:53
@author: seraph★776
project: Codeguppy
metadoc: Calculate 10!
"""


def solution(n):
    if n == 1:
        return n
    return n * solution(n - 1)


if __name__ == '__main__':
    print(solution(10))

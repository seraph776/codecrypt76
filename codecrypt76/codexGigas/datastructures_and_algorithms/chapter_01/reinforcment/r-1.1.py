#!/usr/bin/env python3
"""
created: 2023/06/10 18:32:56
@author: seraph★776
project: Data Structures and Algorithms
metadoc: Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, m % ni == 0 for some integer i, and False otherwise
"""


def solve(n, m):
    return m % n == 0


if __name__ == '__main__':
    samples = [n for n in range(100)]
    results = []
    num = 20
    for s in samples:
        if solve(num, s):
            results.append(s)
    print(results)

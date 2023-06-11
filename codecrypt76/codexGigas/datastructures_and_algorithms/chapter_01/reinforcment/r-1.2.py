#!/usr/bin/env python3
"""
created: 2023/06/11 06:30:00
@author: seraph★776
project: Data Structures and Algorithms
metadoc: Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""


def solve(n):
    return ~n & 1


if __name__ == '__main__':
    samples = [i for i in range(10)]
    results = []
    for s in samples:
        if solve(s):
            results.append(s)
    print(results)

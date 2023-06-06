#!/usr/bin/env python3
"""
created: 2023/06/06 09:49:31
@author: seraph★776
project: Codewars
"""
import random


def solution(n):
    return n / 5 == (n * 2) / 10


if __name__ == '__main__':
    samples = [random.randint(1, 50) for i in range(21)]

    for n in samples:
        print(solution(n))
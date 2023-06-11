#!/usr/bin/env python3
"""
created: 2023/06/11 14:44:27
@author: seraph★776
project: Python Crash Course
metadoc: 5-11. Ordinal Numbers
"""


class OrdinalNumbers:
    def __init__(self, n):
        self.n = n

    def solution(self):
        ht = {1: 'st', 2: 'nd', 3: 'rd'}
        if len(str(self.n)) < 2 or self.n in [11, 12, 13]:
            suffix = ht.get(self.n, 'th')
            return f'{self.n}{suffix}'
        else:
            last_digit = self.n % 10
            suffix = ht.get(last_digit, 'th')
            return f'{self.n}{suffix}'


if __name__ == '__main__':
    samples = [n for n in range(1, 32)]
    for i in samples:
        print(OrdinalNumbers(i).solution())

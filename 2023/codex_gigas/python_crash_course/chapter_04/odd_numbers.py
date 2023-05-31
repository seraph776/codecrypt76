#!/usr/bin/env python3
"""
created: 2023/05/31 19:46:27
@author: seraph★776
project: Python Crash Course
metadoc: 4-6. Odd Numbers
"""


class OddNumbers:
    def __init__(self, ):
        self.output = ''

    def solution(self):
        for n in range(1, 21, 2):
            self.output += f'{str(n)}\n'
        return self.output


if __name__ == '__main__':
    odd_number = OddNumbers()
    print(odd_number.solution())

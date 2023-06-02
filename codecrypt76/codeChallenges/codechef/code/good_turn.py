#!/usr/bin/env python3
"""
created: 2023/06/02 13:41:33
@author: seraph★776
project: CodeCHef - Good Turn
metadoc: Determine if the roll of the dice is a "Good Turn."
If the sum of d1 and d2 are greater than 6 return YES else return NO.
torrent: https://www.codechef.com/problems/GDTURN
"""


class Problem:
    def __init__(self):
        self.n = int(input())

    def solution(self):
        for i in range(self.n):
            d1, d2 = map(int, input().split())
            result = sum([d1, d2])
            if result > 6:
                print('YES')
            else:
                print('NO')


if __name__ == '__main__':
    problem = Problem()
    problem.solution()

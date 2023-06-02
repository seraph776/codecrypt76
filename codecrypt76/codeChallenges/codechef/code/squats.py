#!/usr/bin/env python3
"""
created: 2023/06/02 14:32:32
@author: seraph★776
project: CodeChef- Squats
metadoc: Each set consists of 15 squats. Given the numbers of sets, determine total number of squats.
"""

SQUAT_SET = 15


class Problem:
    def __init__(self):
        self.n = int(input())

    def solution(self):
        for i in range(self.n):
            reps = int(input())
            result = reps * SQUAT_SET
            print(result)


if __name__ == '__main__':
    problem = Problem()
    problem.solution()

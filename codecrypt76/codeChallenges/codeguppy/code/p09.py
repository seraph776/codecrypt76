#!/usr/bin/env python3
"""
created: 2023/06/02 17:55:00
@author: seraph★776
project: Codeguppy
metadoc: Create a function that will convert from Fahrenheit to Celsius
"""


def solution(temp):
    return (temp - 32) * 5 / 9


if __name__ == '__main__':
    print(solution(32))
    print(solution(80))

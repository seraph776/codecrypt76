#!/usr/bin/env python3
"""
created: 2023/06/02 17:52:02
@author: seraph★776
project: Codeguppy
metadoc: Create a function that will convert from Celsius to Fahrenheit
"""


def solution(temp):
    return (temp * 9 / 5) + 32


if __name__ == '__main__':
    print(solution(0))
    print(solution(20))

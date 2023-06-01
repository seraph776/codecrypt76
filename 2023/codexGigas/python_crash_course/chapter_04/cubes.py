#!/usr/bin/env python3
"""
created: 2023/05/31 20:45:29
@author: seraph★776
project: Python Crash Course
metadoc: 4-8. Cubes
"""


def cubes():
    result = []
    for n in range(1, 11):
        result.append(n ** 3)
    return result


if __name__ == '__main__':
    print(cubes())

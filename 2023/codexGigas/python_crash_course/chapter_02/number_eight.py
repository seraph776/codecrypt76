#!/usr/bin/env python3
"""
created: 2023/05/27 22:26:22
@author: seraph★776
project: Python Crash Course
metadoc: 2-8. Number Eight
"""


def number_eight():
    output = [
        f'5 + 3 = {5 + 3}',
        f'9 - 1 = {9 - 1}',
        f'8 ÷ 1 = {8 // 1}',
        f'2 * 4 = {2 * 4}',
    ]
    for eight in output:
        print(eight)


if __name__ == '__main__':
    number_eight()

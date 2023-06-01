#!/usr/bin/env python3
"""
created: codecrypt76/05/30 20:02:12
@author: seraph★776
project: Codeguppy
metadoc: Print the multiplication table with 7
"""


def solution():
    output = ''
    for n in range(11):
        output += f'{n} * 7 = {n * 7}\n'
    return output


if __name__ == '__main__':
    print(solution())

#!/usr/bin/env python3
"""
created: 2023/05/30 21:12:22
@author: seraph★776
project: Codeguppy
metadoc: Print all the multiplication tables with numbers from 1 to 10
"""


def solution():
    output = ''
    for n in range(1, 11):
        for m in range(1, 11):
            output += f'{n} * {m} = {n * m}\n'
            print(output)
        #output += '\n'
    return output


if __name__ == '__main__':
    print(solution())


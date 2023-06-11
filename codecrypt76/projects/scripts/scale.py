#!/usr/bin/env python3
"""
created: 2023/06/11 11:02:22
@author: seraph★776
project: None
metadoc: None
"""


def scale(a, b):
 
    if a == b:
        return 'a and b are equal'
    elif a > b:
        return f'a weighs more than b by {a-b} lbs.'
    else:
        return f'b weighs more than a by {abs(b-a)} lbs.'



if __name__ == '__main__':
    print(scale(50, 140))
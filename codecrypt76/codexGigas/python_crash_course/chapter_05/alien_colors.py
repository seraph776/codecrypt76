#!/usr/bin/env python3
"""
created: 2023/06/02 19:06:23
@author: seraph★776
project: Python Crash Course
metadoc: 5-3. Alien Colors #1
"""


def alien_color(color):
    if color == 'red':
        return 5
    elif color == 'green':
        return 10
    elif color == 'blue':
        return 15
    else:
        return 0


if __name__ == '__main__':
    colors = ['yellow', 'red', 'black', 'blue', 'green', 'orange']
    for c in colors:
        print(alien_color(c))

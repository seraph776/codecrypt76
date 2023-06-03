#!/usr/bin/env python3
"""
created: 2023/06/02 19:15:01
@author: seraph★776
project: Python Crash Course
metadoc: 5-3. Alien Colors #2
"""

def alien_color(color):
    d = {'red': 5, 'green':10, 'blue':15}
    if color == 'red':
        return f'player earned 5 points for killing {color} alien.'
    elif color == 'green':
        return f'player earned 10 points for killing {color} alien.'
    elif color == 'blue':
        return f'player earned 15 points for killing {color} alien.'
    else:
        return f'player earned 0 points...'


if __name__ == '__main__':
    colors = ['yellow', 'red', 'black', 'blue', 'green', 'orange']
    for c in colors:
        print(alien_color(c))

#!/usr/bin/env python3
"""
created: 2023/06/02 08:55:12
@author: seraph★776
project: Python Crash Course
metadoc: Conditional Test
"""


def conditional_test(param):
    if isinstance(param, int):
        if param in [7, 11]:
            return 'Lucky Number Sleven'
        elif param % 2 == 0:
            return 'This number is even'
        elif param % 2 == 1:
            return 'This number is odd'
    elif isinstance(param, float):
        if param == 3.14:
            return 'Have some pie'
        else:
            return 'Have a rootbeer float'
    elif isinstance(param, str):
        if param == 'Python':
            return 'Best programming language'
        elif param == 'seraph776':
            return 'Best Python programmer ever!'
        else:
            return sum([ord(i) for i in param])
    elif isinstance(param,(list, tuple)):
        if len(param) <= 3:
            return 'This sequence is greater than or equal to three.'
        elif len(param) == 12:
            return 'This sequence has a dozen elements.'
        elif len(param) > 12:
            return 'This sequence is greater than a dozen.'
        else:
            return f'Yahtzee!: {param[0]*"*"}'



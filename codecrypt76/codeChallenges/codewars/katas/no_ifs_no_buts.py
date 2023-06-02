#!/usr/bin/env python3
"""
created: 2023/06/02 18:12:50
@author: seraph★776
project: Codewars - No ifs no buts
metadoc: Write a function that accepts two numbers a and b and returns whether a is smaller than,
bigger than, or equal to b, as a string; example:
    (5, 4)   ---> "5 is greater than 4"
    (-4, -7) ---> "-4 is greater than -7"
    (2, 2)   ---> "2 is equal to 2"

Exception: Cannot use "if" or ternary operators
source: https://www.codewars.com/kata/592915cc1fad49252f000006/train/python
"""


def no_ifs_no_buts(a, b):
    match (a > b, a < b, a == b):
        case (True, _, _):
            return f'{a} is greater than {b}'
        case (_, True, _):
            return f'{a} is smaller than {b}'
        case (_, _, True):
            return f'{a} is equal to {b}'

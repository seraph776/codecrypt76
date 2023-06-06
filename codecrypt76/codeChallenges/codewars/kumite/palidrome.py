#!/usr/bin/env python3
"""
created: 2023/06/04 21:14:04
@author: seraph★776
project: Codewars Kumite
"""

import string


def is_palindrome(s: str) -> bool:
    s = s.replace(' ', '').lower().translate(str.maketrans('', '', string.punctuation))
    return s == s[::-1]



print(is_palindrome('Won\'t lovers revolt now?'))

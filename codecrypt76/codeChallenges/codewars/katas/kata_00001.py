#!/usr/bin/env python3
"""
created: 2023/06/07 21:21:40
@author: seraph★776
project: None
metadoc: None
"""


def second_symbol(s, symbol):
    s = s.replace(symbol, '', 1)
    return -1 if symbol not in s else s.index(symbol) + 1


if __name__ == '__main__':
    print(second_symbol('','q'))


#!/usr/bin/env python3
"""
created: 2023/05/27 19:22:24
@author: seraph★776
project: Python Crash Course
metadoc: 2-5. Famous Quote #1
"""


def famous_quote():
    person = 'friedrich nietzsche'
    quote = 'That which does not kill us makes us stronger'
    return f'{person.title()} once said, "{quote}."'


if __name__ == '__main__':
    print(famous_quote())

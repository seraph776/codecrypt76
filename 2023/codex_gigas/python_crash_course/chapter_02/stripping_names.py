#!/usr/bin/env python3
"""
created: 2023/05/27 22:04:08
@author: seraph★776
project: project: Python Crash Course
metadoc: 2-7. Stripping Names:
"""


class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        return f'{self.first_name} {self.last_name}'.title()


def stripping_name():
    first = input('Enter your first name:\n> ')
    last = input('Enter last name:\n> ')

    def buffer(n):
        n = f'\t{n}\t'
        return n

    name = Name(first, last).display()
    name = buffer(name)

    protocol = {'lstrip:': f'.{name.lstrip()}.',
                'rstrip:': f'.{name.rstrip()}.',
                'strip:': f'.{name.strip()}.',
                }
    for k, v in protocol.items():
        print(k, v)


if __name__ == '__main__':
    stripping_name()

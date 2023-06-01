#!/usr/bin/env python3
"""
created: codecrypt76/05/27 18:25:53
@author: seraph★776
project: Python Crash Course
metadoc: 2-3. Personal Message:
"""


def personal_message(name: str) -> str:
    return f'Hello {name.title()}!'


if __name__ == '__main__':
    while user_input := input('Enter your name:\n> '):
        print(personal_message(user_input))

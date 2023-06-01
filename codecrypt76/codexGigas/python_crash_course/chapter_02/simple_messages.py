#!/usr/bin/env python3
"""
created: codecrypt76/05/27 18:18:13
@author: seraph★776
project: Python Crash Course
metadoc: 2-2. Simple Messages:
"""

from simple_message import simple_message as simp


def simple_messages(func):
    def wrapper():
        msg = func()[5:]
        new_msg = 'Goodbye' + msg
        return new_msg
    return wrapper()


if __name__ == '__main__':
    print(simple_messages(simp))

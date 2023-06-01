#!/usr/bin/env python3
"""
created: 2023/05/30 13:21:08
@author: seraph★776
project: Python Crash Course
metadoc: 4-3. Counting to Twenty
"""


class TwentyCount:
    def __init__(self):
        self.counter = 0

    def count_for(self):
        self.counter = 0
        for n in range(21):
            self.counter += 1
            print(self.counter)
        print('Complete!')

    def count_while(self):
        self.counter = 0
        while self.counter != 21:
            self.counter += 1
            print(self.counter)
        print('Complete!')


if __name__ == '__main__':
    count = TwentyCount()
    count.count_while()
    count.count_for()

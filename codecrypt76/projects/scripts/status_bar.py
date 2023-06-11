#!/usr/bin/env python3
"""
created: 2023/06/11 09:21:33
@author: seraph★776
project: Satus Bar
"""

import time
from tqdm import tqdm


class StatusBar:
    def __init__(self, total_time, increment):
        self.total_time = total_time
        self.increment = increment

    def display(self):
        for _ in tqdm(range(self.total_time)):
            time.sleep(self.increment)


if __name__ == '__main__':
    StatusBar(10, 2).display()


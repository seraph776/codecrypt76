#!/usr/bin/env python3
"""
created: 2023/06/02 11:56:03
@author: seraph★776
project: Fortune Teller
"""

import random


def fortune_teller(question):
    answer = random.choice(['yes', 'no', 'maybe so'])
    print(f'Question:  {question}?')
    print(f'Answer: {answer}')


if __name__ == '__main__':
    while user_input := input('Ask your question:\n> '):
        fortune_teller(user_input)

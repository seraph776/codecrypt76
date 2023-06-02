#!/usr/bin/env python3
"""
created: 2023/06/02 08:55:12
@author: seraph★776
project: Python Crash Course
metadoc: Conditional Test
"""
import unittest


def conditional_test(param):
    if isinstance(param, int):
        if param in [7, 11]:
            return 'Lucky Number Sleven.'
        elif param % 2 == 0:
            return 'This number is even.'
        elif param % 2 == 1:
            return 'This number is odd.'
    elif isinstance(param, float):
        if param == 3.14:
            return 'Have some pie!'
        else:
            return 'Have a rootbeer float.'
    elif isinstance(param, str):
        if param == 'Python':
            return 'Best programming language!'
        elif param == 'seraph776':
            return 'Best Python programmer ever!'
        else:
            return sum([ord(i) for i in param])
    elif isinstance(param, (list, tuple)):
        if len(param) <= 3:
            return 'This sequence is less than or equal to three.'
        elif len(param) == 12:
            return 'This sequence has a dozen elements.'
        elif len(param) > 12:
            return 'This sequence is greater than a dozen.'
        else:
            return f'Yahtzee!: {param[0] * "*"}'


class TestConditionTest(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(conditional_test(7), 'Lucky Number Sleven.')
        self.assertEqual(conditional_test(11), 'Lucky Number Sleven.')
        self.assertEqual(conditional_test(13), 'This number is odd.')
        self.assertEqual(conditional_test(2), 'This number is even.')

    def test_floats(self):
        self.assertEqual(conditional_test(3.14), 'Have some pie!')
        self.assertEqual(conditional_test(125.000001), 'Have a rootbeer float.')
        self.assertEqual(conditional_test(314.1), 'Have a rootbeer float.')

    def test_string(self):
        sample = 'Javascript'
        self.assertEqual(conditional_test(sample), sum([ord(i) for i in sample]))
        sample = 'seraph776'
        self.assertEqual(conditional_test(sample), 'Best Python programmer ever!')
        sample = 'Python'
        self.assertEqual(conditional_test(sample), 'Best programming language!')

    def test_sequence(self):
        s1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        s2 = [1, 2, 3]
        s3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(conditional_test(s1), f'Yahtzee!: {s1[0] * "*"}')
        self.assertEqual(conditional_test(s2), 'This sequence is less than or equal to three.')
        self.assertEqual(conditional_test(s3), 'This sequence has a dozen elements.')


if __name__ == '__main__':
    unittest.main()

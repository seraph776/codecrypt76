#!/usr/bin/env python3
"""
created: codecrypt76/05/28 23:22:49
@author: seraph★776
project: Codewars Kumite
metadoc: Got this idea from: https://twitter.com/iluminatibot/status/1662896588149207042
"""


# constant
INFINITE_EIGHT = 8


def magick_number_pyramid() -> list:
    """Prints mysterious number pyramid pattern"""
    output = []
    for novem_cycle in range(1, 10):
        left_side = f"{''.join(map(str, range(1, novem_cycle + 1))):>10}"
        middle = f'* {INFINITE_EIGHT} + {novem_cycle}'
        right_side = f'{eval(f"{left_side}{middle}")}'
        equation = f'{left_side}{middle} = {right_side}'
        print(equation)
    return output


if __name__ == '__main__':
    magick_number_pyramid()































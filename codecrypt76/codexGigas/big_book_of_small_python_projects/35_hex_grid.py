#!/usr/bin/env python3
"""
created: codecrypt76/05/31 21:06:50
@author: seraph★776
project: Big Book of Small Python Projects
metadoc: Hex Grid
"""

# Set up constants
# (!) Try changing these values to other numbers:
X_REPEAT = 19  # How many times to tessellate horizontally
Y_REPEAT = 25  # How many times to tessellate vertically


def main():
    for y in range(Y_REPEAT):
        # Display the top half of the hexagon:
        for x in range(X_REPEAT):
            print(r'/\_', end='')
        print()

        # Display the bottom half of the hexagon
        for x in range(X_REPEAT):
            print(r'\_/', end='')
        print()


if __name__ == '__main__':
    main()

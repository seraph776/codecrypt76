#!/usr/bin/env python3
"""
created: 2023/05/30 20:43:49
@author: seraph★776
project: Big Book of Small Python Projects
metadoc: Bitmap Message
"""

import sys

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""


def main():
    print('Bitmap Message')
    print('Enter a message to display with the bitmap.')
    message = input('> ')
    if message == '':
        sys.exit()

    # Loop over each line in the bitmap
    for line in bitmap.splitlines():
        # loop over each character in teh line:
        for i, bit in enumerate(line):
            if bit == ' ':
                # print an empty space since there's a space in the bitmap:
                print(' ', end='')
            else:
                # Print a character from the message
                print(message[i % len(message)], end='')
        print()  # Print a newline.


if __name__ == '__main__':
    main()

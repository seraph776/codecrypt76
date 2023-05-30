#!/usr/bin/env python3
"""
created: 2023/05/29 14:03:25
@author: seraph★776
project: Python Crash Course
metadoc: 3-7. Shrinking Guest List
"""


def shrinking_guest_list(filename):
    with open(filename) as file_obj:
        guests = [i.strip() for i in file_obj]
        while len(guests) != 2:
            removed_guest = guests.pop()
            print(f'{removed_guest.title()} will not be coming to the party tonight!')

        for guest in guests:
            print(f' - {guest.title()} is still coming to the party!')

        print('Deleting last two guest...')
        del guests[0]
        del guests[0]
        print(f'Guest list is now empty: {guests}')

if __name__ == '__main__':
    shrinking_guest_list('data/guests.txt')
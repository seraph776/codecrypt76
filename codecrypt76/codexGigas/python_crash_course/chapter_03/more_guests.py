#!/usr/bin/env python3
"""
created: codecrypt76/05/28 18:44:18
@author: seraph★776
project: Python Crash Course
metadoc: 3-6. More Guests
"""


def more_guests(filename):
    with open(filename) as file_obj:
        guests = [i.strip() for i in file_obj]
    print('More guest will be coming to the party...')
    guest_1 = 'albert einstein'
    guests.insert(0, guest_1)

    guest_2 = 'darth vader'
    guests.insert(len(guests) // 2, guest_2)

    guest_3 = 'jesus christ'
    guests.append(guest_3)

    for guest in guests:
        print(f' - {guest.title()} is coming to the party!')


if __name__ == '__main__':
    more_guests('data/guests.txt')

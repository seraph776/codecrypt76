#!/usr/bin/env python3
"""
created: codecrypt76/05/28 18:15:44
@author: seraph★776
project: Python Crash Course
metadoc: 3-4. Guest List
"""


def guest_list(filename):
    with open(filename) as file_obj:
        guests = [i.strip() for i in file_obj]

    for guest in guests:
        print(f'{guest.title()} is invited to the party tonight.')


if __name__ == '__main__':
    guest_list('data/guests.txt')
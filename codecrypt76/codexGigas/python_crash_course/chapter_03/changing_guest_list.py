#!/usr/bin/env python3
"""
created: codecrypt76/05/28 18:27:16
@author: seraph★776
project: Python Crash Course
metadoc: 3-5. Changing Guest List
"""


def changing_guest_list(filename):
    with open(filename) as file_obj:
        guests = [i.strip() for i in file_obj]

    no_show = guests.pop(0)
    print(f'{no_show.title()} will not make it to the party tonight.')
    new_guest = 'albert einstein'
    print(f'{new_guest.title()} will take come instead.\n')
    guests.insert(0, new_guest)
    for guest in guests:
        print(f'{guest.title()} will be coming to the party tonight!')


if __name__ == '__main__':
    changing_guest_list('data/guests.txt')

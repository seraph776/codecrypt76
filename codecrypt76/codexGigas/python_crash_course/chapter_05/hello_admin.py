#!/usr/bin/env python3
"""
created: 2023/06/05 18:42:25
@author: seraph★776
project: Python Crash Course
metadoc: 5-8. Hello Admin
"""


def get_users(filename):
    with open(filename) as fo:
        return [i.strip() for i in fo]


def hello_admin(users: list):
    for user in users:
        if user == 'admin':
            print(f'>>> Hello {user}! Would you like to see a status report!')
        else:
            print(f'Hello {user}, thank you for logging in again!')


if __name__ == '__main__':
    user_lst = get_users('data/users.txt')
    hello_admin(user_lst)

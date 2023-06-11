#!/usr/bin/env python3
"""
created: 2023/06/11 14:45:24
@author: seraph★776
project: Python Crash Course
metadoc:5-10. Checking Usernames
"""


def get_users(filename):
    with open(filename) as fo:
        return [i.strip() for i in fo]


def login():
    user_list = get_users('data/users.txt')
    while True:
        while True:
            username = input('Please neter your username:\n> ')
            if username not in user_list:
                print('Invalid username')
                continue
            else:
                break
        while True:
            password = input(f'Please enter password for {username}:\n> ')
            if username == 'admin':
                if password == 's3cr3t':
                    break
                else:
                    print(f'Invalid password for {username}!')
                    continue
            elif not username == 'admin':
                if password == 'password':
                    break
                else:
                    print(f'Invalid password for {username}!')
                    continue
            else:
                break
        break
    return username


def hello_admin(users: list):
    username = login()
    if username == 'admin':
        print(f'>>> Hello {username}! Would you like to see a status report!')
    else:
        print(f'Hello {username}, thank you for logging in again!')


if __name__ == '__main__':
    user_lst = get_users('data/users.txt')
    hello_admin(user_lst)

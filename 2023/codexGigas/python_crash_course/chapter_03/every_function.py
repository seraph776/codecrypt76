#!/usr/bin/env python3
"""
created: 2023/05/28 18:37:46
@author: seraph★776
project: Python Crash Course
metadoc: 3-10. Every Function
"""


class SwissArmyList:
    def __init__(self):
        self.swiss_list = []

    def __str__(self):
        return f'{self.swiss_list}'

    def __len__(self):
        return len(self.swiss_list)

    def append(self, data):
        self.swiss_list.append(data)

    def insert(self, ind, data):
        self.swiss_list.insert(ind, data)

    def sort(self):
        self.swiss_list.sort()

    def sorted(self):
        return sorted(self.swiss_list)

    def reverse(self):
        self.swiss_list.sort(reverse=True)

    def delete(self, ind):
        if ind < len(self.swiss_list):
            del self.swiss_list[ind]
            print('Item deleted!')
        elif ind > len(self.swiss_list) - 1:
            print('Index out of range!')
        else:
            print('There is not list')

    def pop(self, ind):
        return self.swiss_list.pop(ind)

    def remove(self, item):
        if item in self.swiss_list:
            self.swiss_list.remove(item)
        else:
            print('Item not in list!')


if __name__ == '__main__':
    every_function = SwissArmyList()
    for n in range(10):
        every_function.append(n)
    print(every_function)
    every_function.insert(0, 1776)
    every_function.insert(len(every_function), 13)
    print(every_function)
    new_sorted_lst = every_function.sorted()
    print(every_function)
    print(new_sorted_lst)
    every_function.reverse()
    print(every_function)
    every_function.delete(len(every_function) - 1)  # deleting last element
    print(every_function)
    every_function.delete(76)  # Index out of range
    every_function.remove('1776')  # Item not in list
    every_function.remove(1776)
    print(every_function)

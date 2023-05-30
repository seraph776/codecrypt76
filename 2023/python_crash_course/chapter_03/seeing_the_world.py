#!/usr/bin/env python3
"""
created: 2023/05/29 14:09:44
@author: seraph★776
project: Python Crash Course
metadoc: 3-8. Seeing the World
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        val = self.head
        while val is not None:
            print(val.data)
            val = val.link

    def sort(self):
        temp = []
        val = self.head
        while val is not None:
            temp.append(val.data)
            val = val.link
        temp.sort()
        return temp


if __name__ == '__main__':
    world_list = LinkedList()
    world_list.head = Node('USA')
    country2 = Node('Brazil')
    country3 = Node('Russia')
    country4 = Node('Germany')
    country5 = Node('Japan')
    country6 = Node('Australia')
    country7 = Node('Italy')

    world_list.head.link = country2
    country2.link = country3
    country3.link = country4
    country4.link = country5
    country5.link = country6
    country6.link = country7

    world_list.display()
    print(world_list.sort())

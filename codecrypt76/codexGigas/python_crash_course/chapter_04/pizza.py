#!/usr/bin/env python3
"""
created: codecrypt76/05/30 02:18:48
@author: seraph★776
project: Python Crash Course
metadoc: 4-1. Pizzas
"""


class Pizza:
    def __init__(self):
        self.toppings = []

    def __str__(self):
        return f'{self.toppings}'

    def __len__(self):
        return len(self.toppings)

    def add_toppings(self, topping):
        self.toppings.append(topping)
        print(f'adding {topping}.')

    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)
            print(f'{topping} removed.')
        else:
            print('Topping not on pizza')


if __name__ == '__main__':
    my_pizza = Pizza()
    with open('data/toppings.txt') as fo:
        toppings = [i.strip() for i in fo]
    for t in toppings:
        my_pizza.add_toppings(t)
    print(my_pizza)

    for topping in my_pizza.toppings:
        print(f'I like {topping} pizza!')
    print(' - I love all pizza!!')
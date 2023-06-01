#!/usr/bin/env python3
"""
created: 2023/06/01 15:49:03
@author: seraph★776
project: Python Crash Course
metadoc: 4-11. My Pizzas, Your Pizzas
"""


from pizza import Pizza


def get_toppings(filename):
    with open(filename) as fo:
        return [i.strip() for i in fo]

pizza_toopings = get_toppings('data/toppings.txt')

my_pizza = Pizza()
your_pizza = Pizza()


for topping in pizza_toopings:
    my_pizza.add_toppings(topping)
    your_pizza.add_toppings(topping)

print('Your pizza', your_pizza)
print('My pizza', my_pizza)

# Make changes to your pizza
your_pizza.remove_topping('mushrooms')
your_pizza.remove_topping('hamburger')
your_pizza.add_toppings('pineapple')
your_pizza.add_toppings('anchovies')
del your_pizza.toppings[0]
# Make change sto my pizza
my_pizza.remove_topping('mushrooms')
my_pizza.add_toppings('magick mushrooms')
my_pizza.remove_topping('hamburger')
my_pizza.add_toppings('steak')
my_pizza.remove_topping('bacon')

print('Your pizza', your_pizza)
print('My pizza', my_pizza)
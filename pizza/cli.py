#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: arturarakelan
"""
pizzas = ['Margherita', 'Pepperoni', 'Hawaiian']
sizes = ['L', 'XL']
recipts = {'Margherita': ['tomato sauce','mozzarella','tomatoes'],
           'Pepperoni': ['tomato sauce','mozzarella','pepperoni'],
           'Hawaiian': ['tomato sauce','mozzarella','chicken','pineapples']
           }

import click
from Pizza_file import Pizza
import random


def log(text):
    def outer_wrapper(func):
        def inner_wrapper(pizza):
            waiting_time = random.randint(10,50)
            print(text.format(waiting_time)) 
        return inner_wrapper
    return outer_wrapper


@log('🍳 Приготовили за {}с!')
def bake(pizza):
    """Готовит пиццу"""
    return random.randint(10,50)


@log('🛵 Доставили за {}с!')
def delivery_pizza(pizza):
    """Доставляет пиццу"""
    return random.randint(10,50)


@log('🏡 Забрали за {}с!')
def pickup(pizza):
    """Самовывоз"""
    return random.randint(10,50)


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza')
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    bake(pizza)
    if delivery is False:
        delivery_pizza(pizza)
    else:
        pickup(pizza)


@cli.command()
def menu():
    """
    Выводит меню
    """
    for pizza in pizzas:
        recipt = Pizza(pizza, 'L').__dict__()
        print(f'- {recipt}. Рзамеры: L/XL')


if __name__ == '__main__':
    cli()
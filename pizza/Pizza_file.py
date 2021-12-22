#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: arturarakelan
"""
import random
import abc


pizzas = ['Margherita', 'Pepperoni', 'Hawaiian']
sizes = ['L', 'XL']
recipts = {'Margherita': ['tomato sauce','mozzarella','tomatoes'],
           'Pepperoni': ['tomato sauce','mozzarella','pepperoni'],
           'Hawaiian': ['tomato sauce','mozzarella','chicken','pineapples']
           }

class Pizza:
    """
    Создается абстрактный класс для всех видов пицц 🍕, но ....... 
    """
    #@abc.abstractmethod
    def __init__(self, pizza: str, size: str):
        if (pizza in pizzas) and (size in sizes):
            self.name = pizza 
            self.size = size
        else:
            offer_pizza = random.choice(pizzas)
            offer_size = random.choice(sizes)
            raise ValueError(f'Может попробовать {offer_pizza} размером {offer_size}?')
    
   #@abc.abstractmethod
    def __dict__(self):
        """
        метод __dict__() выводит рецепт в виде словаря
        """
        recipt = recipts[self.name]
        print('Рецепт ниже')
        return {self.name: recipt}  
    
    def __eq__(self, other):
        """
        Проверка равенства названий и размера пицц
        """
        return self.name == other.name and self.size == other.size
     
class Margherita(Pizza):
    """
    Класс Маргарита 🧀
    """

    def __init__(self, pizza: str, size: str):
        super().__init__(self.name, self.size)
        
class Pepperoni(Pizza):
    """
    Класс Пепперони 🍕
    """

    def __init__(self, pizza: str, size: str):
        super().__init__(self.name, self.size)

class Hawaiian(Pizza):
    """
    Класс Гавайская 🍍
    """

    def __init__(self, pizza: str, size: str):
        super().__init__(self.name, self.size)
              
if __name__ == '__main__':
    pizza1 = Pizza('Margherita', 'L')
    pizza2 = Pizza('Pepperoni', 'XL')
    pizza3 = Pizza('Margherita', 'XL')
    print(pizza2.__dict__())
    print(pizza1 == pizza3)
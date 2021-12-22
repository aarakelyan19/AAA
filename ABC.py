#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: arturarakelan
"""

import abc
import random


class AnimeMon:
    def __init__(self):
        self._exp = 0
        
    @property
    @abc.abstractmethod
    def exp(self):
        return self._exp
    
    
    @abc.abstractmethod
    def inc_exp(self, value):
        pass

class Pokemon(AnimeMon):
    
    @property
    def exp(self):
        return super().exp

    def inc_exp(self, value):
        self._exp += value * 4
      
        
class Digimon(AnimeMon):

    @property
    def exp(self):
        return super().exp

    def inc_exp(self, value):
        self._exp += value * 8

    
def train(pokemon: Pokemon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - pokemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            pokemon.inc_exp(step_size)


if __name__ == '__main__':
    pokemon = Pokemon()
    digimon = Digimon()
    train(pokemon)
    print(pokemon.exp)
    train(digimon)
    print(digimon.exp)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: arturarakelan
"""

class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self) -> str:
        return f'\033[1;38;2;{self.red};{self.green};{self.blue}m●\033[0m'

    def __repr__(self) -> str:
        return f'\033[1;38;2;{self.red};{self.green};{self.blue}m●\033[0m'    

    def _normalize(self, value):
        return max(min(255, value), 0)

    def __eq__(self, other):
        if self.red == other.red and self.green == other.green and self.blue == other.blue:
            return True
        else:
            raise TypeError('разные')
   
    def __add__(self, other):
        self.red = min(255, self.red + other.red)
        self.green = min(255, self.green + other.green)
        self.blue = min(255, self.blue + other.blue)
        return Color(self.red, self.green, self.blue)
    
    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def contr(self, value, c):
        cl = -256 * (1 - c)
        F = 259 * (cl + 255) / (255 * (259 - cl))
        return int(F * (value - 128) + 128)
    
    def __mul__(self, c):
        cl = -256 * (1 - c)
        f = 259 * (cl + 255) / (255 * (259 - cl))
        red_ = int(f * (self.red - 128) + 128)
        green_ = int(f * (self.green - 128) + 128)
        blue_ = int(f * (self.blue - 128) + 128)
        return Color(red_, green_, blue_)

    def __rmul__(self, c):
        return self.__mul__(c)

def print_a(color: Color):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 +
        [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 +
        [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 +
        [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 +
        [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 +
        [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    red = Color(255, 0, 0)
    print_a(red)
    print_a(0.8 * red)
    print_a(0.6 * red)
    print_a(0.4 * red)
    print_a(0.2 * red)
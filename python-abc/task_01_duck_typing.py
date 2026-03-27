#!/usr/bin/python3
"""
Module for Shape abstract class and its subclasses
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class Shape"""

    @abstractmethod
    def area(self):
        """Abstract method for area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for perimeter"""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape"""

    def __init__(self, radius):
        """Initializes Circle with radius"""
        self.radius = radius

    def area(self):
        """Calculates area of circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates perimeter of circle"""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle class that inherits from Shape"""

    def __init__(self, width, height):
        """Initializes Rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculates area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculates perimeter of rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints area and perimeter using duck typing"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

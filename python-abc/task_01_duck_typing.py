#!/usr/bin/python3
import math
from abc import ABC, abstractmethod

# 1. Abstrakt ana sinif
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# 2. Circle sinfi (Shape-in daxilində yox, kənarında olmalıdır)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# 3. Rectangle sinfi
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# 4. Duck Typing funksiyası
def shape_info(obj):
    # Obyektin növünü yoxlamırıq, sadəcə metodları çağırırıq
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")

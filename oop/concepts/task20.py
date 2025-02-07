# Polymorphism
import math


class Shape:
    def calc_are(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calc_are(self):
        return math.pi * pow(self.radius, 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_are(self):
        return self.width * self.height


shapes = [Circle(8), Rectangle(8, 10), Circle(7), Rectangle(4, 5)]

for shape in shapes:
    print(shape.calc_are())

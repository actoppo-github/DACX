__author__ = 'Arnold C. Toppo'

import math


# class ShapeVolume:


class RegularPolygon:
    def __init__(self, num_sides, side_length, length):
        self.num_sides = num_sides
        self.side_length = side_length
        self.length = length

    def area(self):
        if self.num_sides < 3:
            return "Invalid number of sides. A polygon must have at least 3 sides."

        if self.side_length <= 0:
            return "Invalid side length. The length must be greater than zero."

        # Calculate the area of the regular polygon using the formula: area = (s^2 * n) / (4 * tan(pi/n))
        area = (self.side_length ** 2 * self.num_sides) / (4 * math.tan(math.pi / self.num_sides))

        return area

    def volume(self):
        if self.length <= 0:
            return "Invalid length. The height must be greater than zero."

        # Calculate the area of the base (the regular polygon)
        area_base = self.area()

        # Calculate the volume using the formula: volume = area_base * height
        volume = area_base * self.length

        return volume


class Rectangle:
    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length

    def area(self):
        if self.height <= 0 or self.width <= 0:
            return "Invalid dimensions. Length and width must be greater than zero."

        # Calculate the area of the rectangle using the formula: area = length * width
        area = self.height * self.width

        return area

    def volume(self):
        if self.length <= 0:
            return "Invalid length. The height must be greater than zero."

        # Calculate the area of the base (the regular polygon)
        area_base = self.area()

        # Calculate the volume using the formula: volume = area_base * height
        volume = area_base * self.length

        return volume


class Circle:
    def __init__(self, radius, length):
        self.radius = radius
        self.length = length

    def area(self):
        if self.radius <= 0:
            return "Invalid radius. The radius must be greater than zero."

        # Calculate the area of the circle using the formula: area = pi * radius^2
        area = math.pi * (self.radius ** 2)

        return area

    def volume(self):
        if self.length <= 0:
            return "Invalid length. The height must be greater than zero."

        # Calculate the area of the base (the regular polygon)
        area_base = self.area()

        # Calculate the volume using the formula: volume = area_base * height
        volume = area_base * self.length

        return volume

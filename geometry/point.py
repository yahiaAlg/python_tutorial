from math import sqrt
from operator import __add__

from vector import Vector


class Point:
    def __init__(self) -> None:
        self.name = "O"
        self.__coord_x = 0
        self.__coord_y = 0

    def __init__(self, name, x, y) -> None:
        self.name = name
        self.__coord_x = x
        self.__coord_y = y

    def from_point(self, name, point) -> None:
        self.name = name
        self.__coord_x = point.__coord_x
        self.__coord_y = point.__coord_y

    def __str__(self) -> str:
        return f"{self.name}({self.__coord_x},{self.__coord_y})"

    def set_name(self, given_name):
        self.name = given_name

    @property
    def coord_x(self):
        return self.__coord_x

    @property
    def coord_y(self):
        return self.__coord_y

    @property
    def from_origin(self):
        return sqrt(self.coord_x**2 + self.coord_y**2)

    def set_name(self, given_name):
        self.name = given_name

    def set_x(self, x):
        self.__coord_x = x

    def set_y(self, y):
        self.__coord_y = y

    def set_coordinates(self, point: object):
        self.__coord_x = point.coord_x
        self.__coord_y = point.coord_y

    def __eq__(self, __value: object) -> bool:
        return self.coord_x == __value.coord_x and self.coord_y == __value.coord_y

    def __add__(self, __value: object):
        return Point("", self.coord_x + __value.coord_x, self.coord_y + __value.coord_y)

    def addition(self, obj: object) -> bool:
        return Point("", self.coord_x + obj.coord_x, self.coord_y + obj.coord_y)

    def __sub__(self, __value: object) -> bool:
        return Point("", self.coord_x - __value.coord_x, self.coord_y - __value.coord_y)

    def scale(self, factor):
        return Point("scaled point", self.coord_x * factor, self.coord_y * factor)

    def translation(self, vector: Vector):
        return Point(
            "new point", self.coord_x + vector.comp_i, self.coord_y + vector.comp_j
        )

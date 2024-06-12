from math import sqrt
from operator import __add__
from pprint import pprint


class Vector:
    def __init__(self) -> None:
        self.name = "O"
        self.__comp_i = 0
        self.__comp_j = 0

    def __init__(self, name, x, y) -> None:
        self.name = name
        self.__comp_i = x
        self.__comp_j = y

    def from_point(self, name, point) -> None:
        self.name = name
        self.__comp_i = point.__comp_i
        self.__comp_j = point.__comp_j

    def __str__(self) -> str:
        return f"{self.name}({self.__comp_i},{self.__comp_j})"

    @property
    def comp_i(self):
        return self.__comp_i

    @property
    def comp_j(self):
        return self.__comp_j

    @property
    def magnitude(self):
        return sqrt(self.comp_i**2 + self.comp_j**2)

    def set_name(self, given_name):
        self.name = given_name

    def set_i(self, i):
        self.__comp_i = i

    def set_j(self, j):
        self.__comp_j = j

    def set_components(self, vector: object):
        self.__comp_i = vector.comp_i
        self.__comp_j = vector.comp_j

    def __eq__(self, __value: object) -> bool:
        return self.comp_i == __value.comp_i and self.comp_j == __value.comp_j

    def __add__(self, __value: object):
        return Vector("", self.comp_i + __value.comp_i, self.comp_j + __value.comp_j)

    def addition(self, obj: object) -> bool:
        return Vector("", self.comp_i + obj.comp_i, self.comp_j + obj.comp_j)

    def __sub__(self, __value: object) -> bool:
        return Vector("", self.comp_i - __value.comp_i, self.comp_j - __value.comp_j)

    def scale(self, factor):
        return Vector(self.name, self.comp_i * factor, self.comp_j * factor)

    def translation(self, vector: object):
        return Vector(
            "new vector", self.comp_i + vector.comp_i, self.comp_j + vector.comp_j
        )


class UniteVector(Vector):
    def __init__(self, name, x, y) -> None:
        super().__init__(name, x, y)

        print(self.comp_i)
        print(self.comp_j)
        print(self.name)
        if not (self.comp_i <= 1 and self.comp_j <= 1):
            self.set_i(self.comp_i / self.magnitude)
            self.set_j(self.comp_j / self.magnitude)

import math


class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"<{self.__x}, {self.__y}>"

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def distance(self):
        return math.sqrt(self.__x ** 2 + self.__y ** 2)

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    @classmethod
    def unit_vector(cls):
        return cls(1, 1)

    @staticmethod
    def calculate_distance(tup1, tup2):
        return math.sqrt((tup2[0] - tup1[0]) ** 2 + (tup2[1] - tup1[1]) ** 2)


vector = Vector(2, 2)
print(vector)
# <2, 2>
print(vector.distance)
# 2.8284271247461903
unit_vector = Vector.unit_vector()
print(unit_vector)
# <1, 1>
unit_vector.x = 3
unit_vector.y = 3
print(unit_vector)
# <3, 3>
print(Vector.calculate_distance((3, 6), (6, 8)))
# 3.605551275463989
print(vector.calculate_distance((3, 6), (6, 8)))
# 3.605551275463989
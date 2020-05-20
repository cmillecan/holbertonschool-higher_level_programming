#!/usr/bin/python3
"""Class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes data"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    """Returns the area of a square"""
    def area(self):
        return self.__size ** 2

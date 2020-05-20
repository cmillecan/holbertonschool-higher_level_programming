#!/usr/bin/python3
"""Class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes data"""
        self.size = size

    def area(self):
        """Returns the area of a square"""
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

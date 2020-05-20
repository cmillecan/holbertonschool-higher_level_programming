#!/usr/bin/python3
"""Class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes data"""
        self.size = size

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

    def area(self):
        """Returns the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square"""
        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()

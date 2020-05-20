#!/usr/bin/python3
"""Class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves position"""
        return self.__position

    @size.setter
    def position(self, value):
        """Property setter"""
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int\
                or type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns area of square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square"""
        print('\n' * self.__position[1], end=""))
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
        if self.__size == 0:
            print()

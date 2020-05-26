#!/usr/bin/python3
""" Class """


class Rectangle:
    """ Defines a rectangle """

    def __init__(self, width=0, height=0):
        """Define width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """Retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """Returns area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints rectangle"""
        if self.__width is 0 or self.__height is 0:
            return ''
        string = ('#' * self.__width + '\n') * self.__height
        return string[:-1]

    def __repr__(self):
        """Returns a string representation of rectangle"""
        new_rec = (self.__width, self.__height)
        return 'Rectangle' + str(new_rec)

    def __del__(self):
        """Delete"""
    print('Bye rectangle...')

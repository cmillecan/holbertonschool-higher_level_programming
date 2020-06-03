#!/usr/bin/python3
"""
Rectangle module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.width)
        self.integer_validator("height", self.height)

    def area(self):
        """
        Area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Print rectangle
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

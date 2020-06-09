#!/usr/bin/python3
""" Rectangle """
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Width of rectangle """
        return self.__width

    @property
    def height(self):
        """ Height of rectangle """
        return self.__height

    @property
    def x(self):
        """ X of rectangle """
        return self.__x

    @property
    def y(self):
        """ Y of rectangle """
        return self.__y

    @width.setter
    def width(self, width):
        """ Width setter """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @height.setter
    def height(self, height):
        """ Height setter """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @x.setter
    def x(self, x):
        """ X setter """
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @y.setter
    def y(self, y):
        """ Y setter """
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """ Area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ Print # """
        for row in range(self.__y):
            print()
        for col in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """ Rectangle as a string """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                 self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.width = args[1]
            if len(args) == 3:
                self.height = args[2]
            if len(args) == 4:
                self.x = args[3]
            if len(args) == 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

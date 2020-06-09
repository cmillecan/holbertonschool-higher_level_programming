#!/usr/bin/python3
""" Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Size getter """
        return self.width

    @size.setter
    def size(self, size):
        """ Size setter """
        self.width = size
        self.height = size

    def __str__(self):
        """ Square as a string """
        return '[Square] ({}) {}/{} - {}'.format(
                self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ Assigns attributes """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

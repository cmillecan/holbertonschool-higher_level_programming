#!/usr/bin/python3
"""
MyInt module
"""

class MyInt(int):
    """
    Inherits from int
    """

    def MyInt():
        def __eq__(self, other):
            """Equal to"""
            return int(self) != int(other)

        def __ne__(self, other):
            """Not equal to"""
            return int(self) == int(other)

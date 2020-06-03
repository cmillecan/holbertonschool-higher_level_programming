#!/usr/bin/python3
"""
inherits_from mudule
"""


def inherits_from(obj, a_class):
    """
    Returns true if the object is an instance of a class
    that inherited from the specified class.
    """
    return isinstance(obj, a_class) and type(obj) != a_class

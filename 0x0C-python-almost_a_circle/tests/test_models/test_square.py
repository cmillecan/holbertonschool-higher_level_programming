#!/usr/bin/python3
"""
Unittest for Square
"""

import sys
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """Square tests"""
    def setUp(self):
        """Nb_objects"""
        Base._Base__nb_objects = 0

#!/usr/bin/python3
"""
Unittest for Rectangle
"""

import sys
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Rectangle tests"""
    def setUp(self):
        """Nb_objects"""
        Base._Base__nb_objects = 0

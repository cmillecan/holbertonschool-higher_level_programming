#!/usr/bin/python3
"""
Unittest for Base
"""

import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Base tests"""
    def setUp(self):
        """Nb_objects"""
        Base._Base__nb_objects = 0

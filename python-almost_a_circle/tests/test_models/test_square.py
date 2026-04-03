#!/usr/bin/python3
"""
Unittest for Square class.
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Define unittests for Square class.
    """

    def test_init(self):
        """Test initialization with size."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_area(self):
        """Test area method inherit from Rectangle."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        """Test __str__ method."""
        s = Square(3, 1, 3, 10)
        self.assertEqual(str(s), "[Square] (10) 1/3 - 3")

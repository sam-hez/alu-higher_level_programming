#!/usr/bin/python3
"""
Unittest for Base class.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Define unittests for Base class.
    """

    def test_id_assignment(self):
        """Test automatic id assignment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_provided_id(self):
        """Test provided id assignment."""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

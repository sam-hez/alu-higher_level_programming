#!/usr/bin/python3
"""
Module 1-square
Defines a Square class with a private size attribute.
"""


class Square:
    """
    A class Square that defines a square by: (based on 0-square.py)
    """

    def __init__(self, size):
        """
        Initializes the square with a size.
        Args:
            size: The size of the square.
        """
        self.__size = size

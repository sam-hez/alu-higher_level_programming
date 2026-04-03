#!/usr/bin/python3
"""
Module 3-square
Defines a Square class with area calculation.
"""


class Square:
    """
    A class Square that defines a square by: (based on 2-square.py)
    """

    def __init__(self, size=0):
        """
        Initializes the square with an optional size.
        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the current square area.
        Returns:
            The area of the square.
        """
        return self.__size ** 2

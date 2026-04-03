#!/usr/bin/python3
"""
Module 4-square
Defines a Square class with getter and setter for size.
"""


class Square:
    """
    A class Square that defines a square by: (based on 3-square.py)
    """

    def __init__(self, size=0):
        """
        Initializes the square with an optional size.
        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.
        Args:
            value (int): The size of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the current square area.
        Returns:
            The area of the square.
        """
        return self.__size ** 2

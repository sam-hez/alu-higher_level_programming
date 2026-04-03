#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a class BaseGeometry with an area method and an integer validator.
"""


class BaseGeometry:
    """
    A class BaseGeometry with an area method and an integer validator.
    """

    def area(self):
        """
        Raises an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value as an integer greater than 0.
        Args:
            name: The name of the parameter.
            value: The value to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

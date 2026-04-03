#!/usr/bin/python3
"""
Module 5-rectangle
Defines a Rectangle class with deletion message.
"""


class Rectangle:
    """
    A class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with optional width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with validation.
        Args:
            value (int): The width of the rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle with validation.
        Args:
            value (int): The height of the rectangle.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.
        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        Returns:
            The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using #.
        Returns:
            The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for i in range(self.__height):
            rect_str += "#" * self.__width
            if i != self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """
        Returns a string representation of the rectangle to be able to
        recreate a new instance by using eval().
        Returns:
            The representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")

#!/usr/bin/python3
"""
This module contains the Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Representation of a Square that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the Square instance.

        Args:
            size (int): The side length of the square.
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            id (int): The identifier of the instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the Square instance with new attributes.

        Args:
            *args (list): No-keyword arguments (id, size, x, y).
            **kwargs (dict): Key-worded arguments.
        """
        if args and len(args) != 0:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Square instance."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

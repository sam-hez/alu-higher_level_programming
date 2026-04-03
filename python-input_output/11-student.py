#!/usr/bin/python3
"""
This module defines a Student class.
"""


class Student:
    """
    Represent a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student with first_name, last_name and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings representing attributes to retrieve.

        Returns:
            dict: The filtered dictionary representation of the student.
        """
        if attrs is None:
            return self.__dict__

        if not isinstance(attrs, list):
            return self.__dict__

        for item in attrs:
            if not isinstance(item, str):
                return self.__dict__

        my_dict = {}
        for key in attrs:
            if key in self.__dict__:
                my_dict[key] = self.__dict__[key]
        return my_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary where keys are attribute names and
                        values are the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)

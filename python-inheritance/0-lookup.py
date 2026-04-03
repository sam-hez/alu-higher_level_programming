#!/usr/bin/python3
"""
Module 0-lookup
Returns the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    Args:
        obj: The object to look up.
    Returns:
        A list of attributes and methods.
    """
    return dir(obj)

#!/usr/bin/python3
"""
This module contains a function that returns an object (Python data
structure) represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        obj: The Python data structure representation.
    """
    return json.loads(my_str)

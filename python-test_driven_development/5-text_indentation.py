#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: The text to be processed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    c = 0
    length = len(text)

    # Skip initial spaces
    while c < length and text[c] == ' ':
        c += 1

    while c < length:
        print(text[c], end="")
        if text[c] in punctuation:
            print("\n")
            c += 1
            while c < length and text[c] == ' ':
                c += 1
            continue
        c += 1

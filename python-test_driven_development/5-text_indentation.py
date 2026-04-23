#!/usr/bin/python3
"""
Module for text indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = True
    for char in text:
        if skip_space and char == " ":
            continue

        skip_space = False
        print(char, end="")

        if char in ".?:":
            print("\n")
            skip_space = True

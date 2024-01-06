#!/usr/bin/python3
"""Defines text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    luda = 0
    while luda < len(text) and text[luda] == ' ':
        luda += 1

    while luda < len(text):
        print(text[luda], end="")
        if text[luda] == "\n" or text[luda] in ".?:":
            if text[luda] in ".?:":
                print("\n")
            luda += 1
            while luda < len(text) and text[luda] == ' ':
                luda += 1
            continue
        luda += 1

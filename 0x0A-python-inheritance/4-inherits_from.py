#!/usr/bin/python3
"""Defines inherited class check func"""


def inherits_from(obj, a_class):
    """Checks if an object is inhereted instance of class.

    Args:
        obj (any): obj to check.
        a_class (type): class to match the type of obj to.
    Returns:
        If obj is  - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

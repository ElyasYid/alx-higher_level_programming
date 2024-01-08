#!/usr/bin/python3
"""Define class & inherited class check func"""


def is_kind_of_class(obj, a_class):
    """Check if obj is instance/inherited instance of class.

    Args:
        obj (any): checked obj
        a_class (type): class to match the type of obj to.
    Returns:
        If obj is  - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False

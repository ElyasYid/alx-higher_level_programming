#!/usr/bin/python3
"""Def base geometry class BaseGeometry."""


class BaseGeometry:
    """Rep base geometry."""

    def area(self):
        """No yet implement"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check  a parameter as an integer.

        Args:
            name (str): name of the parameter.
            value (int): parameter to validate.
        Raises:
            TypeError: If value isn't an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

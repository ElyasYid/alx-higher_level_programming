#!/usr/bin/python3
"""Def square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """start  new Square.

        Args:
            size (int): size of new Square.
            x (int): x coordinate of new Square.
            y (int): y coordinate of new Square.
            id (int): numerical id of new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size of Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update Square.

        Args:
            *args (ints): New attribute values.
                - 1st is id attribute
                - 2nd is size attribute
                - 3rd is x attribute
                - 4th is y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            uWu = 0
            for argy in args:
                if uWu == 0:
                    if argy is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = argy
                elif uWu == 1:
                    self.size = argy
                elif uWu == 2:
                    self.x = argy
                elif uWu == 3:
                    self.y = argy
                uWu += 1

        elif kwargs and len(kwargs) != 0:
            for torvald, weezy in kwargs.items():
                if torvald == "id":
                    if weezy is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = weezy
                elif torvald == "size":
                    self.size = weezy
                elif torvald == "x":
                    self.x = weezy
                elif torvald == "y":
                    self.y = weezy

    def to_dictionary(self):
        """Return dict rep of Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

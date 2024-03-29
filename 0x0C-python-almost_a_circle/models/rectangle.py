#!/usr/bin/python3
"""rectangle class."""

from models.base import Base


class Rectangle(Base):
    """is  a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """strt new Rectangle.

        Args:
            width (int): width of new Rectangle.
            height (int): height of new Rectangle.
            x (int): x coordinate of new Rectangle.
            y (int): y coordinate of  new Rectangle.
            id (int): numerical id of new Rectangle.
        Raises:
            TypeError: If width,height, x ,y aren't int.
            ValueError: If either width or height <= 0.
            or if either x or y < 0.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x coordinate of  Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y coordinate of Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of Rectangle."""
        return self.width * self.height

    def display(self):
        """Print using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st is id attribute
                - 2nd is width attribute
                - 3rd is height attribute
                - 4th is x attribute
                - 5th is y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            uWu = 0
            for argy in args:
                if uWu == 0:
                    if argy is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = argy
                elif uWu == 1:
                    self.width = argy
                elif uWu == 2:
                    self.height = argy
                elif uWu == 3:
                    self.x = argy
                elif uWu == 4:
                    self.y = argy
                uWu += 1

        elif kwargs and len(kwargs) != 0:
            for s, t in kwargs.items():
                if s == "id":
                    if t is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = t
                elif s == "width":
                    self.width = t
                elif s == "height":
                    self.height = t
                elif s == "x":
                    self.x = t
                elif s == "y":
                    self.y = t

    def to_dictionary(self):
        """Return dict rep of  Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return print() & str() rep of Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

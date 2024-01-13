#!/usr/bin/python3

"""defines a base model class"""


class Base:
    """ class Base model

        priveate class attribute:
        __nb_objects(int) = number of instantiated objects
    """
    
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize new base

            Args:
            id (int) = The identity of the new base
        """
        if id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

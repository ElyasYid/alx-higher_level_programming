#!/usr/bin/python3

"""Defines a base model class."""
import json


class Base:
    """Base.

    Represents basis for all other classes for proj

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize new Base.

        Args:
            id (int): identity of new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON serialization of list of dicts.

        Args:
            list_dictionaries (list): list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON serialization of list of objects to file.

        Args:
            list_objs (list): list of inherited Base instances.
        """
        fl_name = cls.__name__ + ".json"
        with open(fl_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                l_dicts = [oBj.to_dictionary() for oBj in list_objs]
                jsonfile.write(Base.to_json_string(l_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returndeserialization of JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string None or empty - empty list.
            Otherwise - Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return class instantied from dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                fresh = cls(1, 1)
            else:
                fresh = cls(1)
            fresh.update(**dictionary)
            return fresh

    @classmethod
    def load_from_file(cls):
        """Return list of classes instantiated from JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If file not exist -  empty list.
            Otherwise - list of instantiated classes.
        """
        f_name = str(cls.__name__) + ".json"
        try:
            with open(f_name, "r") as jsonfile:
                l_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**di) for di in l_dicts]
        except IOError:
            return []

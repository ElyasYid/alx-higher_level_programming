#!/usr/bin/python3
"""Def string to JSON function."""
import json


def to_json_string(my_obj):
    """Return JSON  of a string object."""
    return json.dumps(my_obj)

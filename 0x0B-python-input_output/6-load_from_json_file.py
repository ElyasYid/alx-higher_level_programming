#!/usr/bin/python3
"""function create python object from JSON"""
import json


def load_from_json_file(filename):
    """Create a Python object from JSON file."""
    with open(filename) as f:
        return json.load(f)

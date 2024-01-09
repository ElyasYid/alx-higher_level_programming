#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return dict rep of simple data struct."""
    return obj.__dict__

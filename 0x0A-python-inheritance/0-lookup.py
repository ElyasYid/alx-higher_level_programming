#!/usr/bin/python3
"""Defines a object attribute lookup function."""


def lookup(obj):
    """Return list of objects available attributes."""
    return (dir(obj))

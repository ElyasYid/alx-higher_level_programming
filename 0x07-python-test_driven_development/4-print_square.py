#!/usr/bin/python3
"""Define square printer func"""


def print_square(size):
    """Print square with # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for nelly in range(size):
        [print("#", end="") for kelly in range(size)]
        print("")

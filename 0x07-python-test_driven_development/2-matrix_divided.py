#!/usr/bin/python3
"""Define matrix div func."""


def matrix_divided(matrix, div):
    """Divide  elements of a matrix.

    Args:
        matrix (list): list of lists of ints or floats.
        div (int/float):  divisor.
    Raises:
        TypeError: If  matrix contains non-numbers.
        TypeError: If matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix of the result of function.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(rw, list) for rw in matrix) or
            not all((isinstance(el, int) or isinstance(el, float))
                    for el in [nm for rw in matrix for nm in rw])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(rw) == len(matrix[0]) for rw in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), rw)) for rw in matrix])

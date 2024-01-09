#!/usr/bin/python3
"""Pascal's Triangle function."""


def pascal_triangle(n):
    """Pascal's Triangle of size n.

    Returns list of lists of integers reping the triangle.
    """
    if n <= 0:
        return []

    pasqual = [[1]]
    while len(pasqual) != n:
        pas = pasqual[-1]
        op = [1]
        for tit in range(len(pas) - 1):
            op.append(pas[tit] + pas[tit + 1])
        op.append(1)
        pasqual.append(op)
    return pasqual

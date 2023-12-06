#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nemat = [[t ** 2 for t in row] for row in matrix]
    return nemat

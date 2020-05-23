#!/usr/bin/python3
"""
matix_divided module

"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    Returns a new matrix
    """

    error = 'matrix must be a matrix (list of lists) of integers/floats'
    if len(matrix) == 0 or type(matrix) != list:
        raise TypeError(error)

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

            for ele in len(lists):
                if not isinstance(ele, (int, float)):
                    raise TypeError(error)

    if not isinstance(div, (int, float)):
        raise TypeError(err3)

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [[round(i/div, 2) for i in row] for row in matrix]

    return new

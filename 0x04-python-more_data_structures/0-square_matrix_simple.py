#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for arr in matrix:
        new_arr = []
        for el in arr:
            new_arr.append(el * el)

        new_matrix.append(new_arr)

    return new_matrix

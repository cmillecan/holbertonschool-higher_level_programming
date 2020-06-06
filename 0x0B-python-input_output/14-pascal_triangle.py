#!/usr/bin/python3
""" Task 14 """

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the 
    Pascal’s triangle of n.
    """
    row = [1]
    y = [0]
    empt = []
    for i in range(max(n, 0)):
        empt.append(row)
        row = [l + r for l, r in zip(row + y, y + row)]
    return empt

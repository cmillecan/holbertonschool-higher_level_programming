#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """function that finds a peak"""
    for i in range(len(list_of_integers)):
        if list_of_integers[i] > list_of_integers[i + 1]:
            return i
    return (len(list_of_integers - 1))

#!/usr/bin/python3
def common_elements(set_1, set_2):
    set1 = set(set_1)
    intersect = set1.intersection(set_2)
    intersect_list = list(intersect)
    return intersect_list

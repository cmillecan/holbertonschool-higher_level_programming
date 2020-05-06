#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list
    if idx < 0 or idx >= len(copy):
        return copy

    my_list[idx] = element
    return my_list

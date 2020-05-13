#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not roman_string or not isinstance(roman_string, str):
        return 0
    prev = 0
    current = 0
    total = 0
    for i in roman_string:
        current = dic[i]
        if current > prev:
            total = total + current - (2 * prev)
        else:
            total += current
        prev = current

    return total

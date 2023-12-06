#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dicti = {}
    for p in a_dictionary:
        new_dicti[p] = a_dictionary[p] * 2
    return new_dicti

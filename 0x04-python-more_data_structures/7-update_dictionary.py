#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for ertale in a_dictionary:
            if ertale == key:
                a_dictionary[ertale] = value
    return a_dictionary

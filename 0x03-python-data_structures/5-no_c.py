#!/usr/bin/python3
def no_c(my_string):
    new = my_string.translate({ord(k): None for k in 'cC'})
    return new

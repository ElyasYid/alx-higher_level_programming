#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    r_dec = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r_co = 0
    for i in range(len(roman_string)):
        if i > 0 and r_dec[roman_string[i]] > r_dec[roman_string[i - 1]]:
            r_co += r_dec[roman_string[i]] - 2 * \
                        r_dec[roman_string[i - 1]]
        else:
            r_co += r_dec[roman_string[i]]
    return r_co

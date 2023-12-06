#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    poot = list(a_dictionary.keys())[0]
    loot = a_dictionary[poot]
    for e, y in a_dictionary.items():
        if y > loot:
            loot = y
            poot = e
    return (poot)

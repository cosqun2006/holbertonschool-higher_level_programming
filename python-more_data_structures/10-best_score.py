#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_name = ""
    max_val = 0

    for key in a_dictionary:
        if a_dictionary[key] > max_val:
            max_val = a_dictionary[key]
            best_name = key
    return best_name

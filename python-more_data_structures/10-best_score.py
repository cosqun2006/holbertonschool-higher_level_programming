#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_name = ""
    best_score = -1
    for key in a_dictionary:
        if a_dictionary[key] > best_score:
            best_name = key
    return best_name

#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = []
    set_1 = set(set_1)
    set_2 = set(set_2)
    for item in set_1:
        if item not in set_2:
            new_list.append(item)
    return new_list

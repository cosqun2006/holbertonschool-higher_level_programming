#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_1 = set(set_1)
    set_2 = set(set_2)
    new_list = []
    for item in set_1:
        if item in set_2:
            new_list.append(item)
    return new_list

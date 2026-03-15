#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = []
    for item in my_list:
        new_list.append(item * number)
        number += 1
    return new_list

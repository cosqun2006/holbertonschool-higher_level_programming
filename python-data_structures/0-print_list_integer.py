#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Siyahını tərsinə çeviririk və hər bir elementi 'i' olaraq götürürük
    for i in my_list[::-1]:
        print("{:d}".format(i))

#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    res = 0
    n = len(roman_string)

    for i in range(n):
        val = roman_dict[roman_string[i]]

        if i + 1 < n and roman_dict[roman_string[i + 1]] > val:
            res -= val
        else:
            res += val

    return res

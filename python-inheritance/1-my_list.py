#!/usr/bin/python3
"""
Bu modul list-dən miras alan MyList sinfini təqdim edir.
"""


class MyList(list):
    """
    Standart list sinfinə print_sorted metodunu əlavə edən sinif.
    """

    def print_sorted(self):
        """
        Siyahıdakı elementləri artan sıra ilə çap edir.
        Orijinal siyahını dəyişmir.
        """
        print(sorted(self))

#!/usr/bin/python3
"""
Tələbə (Student) sinfini təyin edən modul.
"""


class Student:
    """
    Tələbə haqqında məlumatları saxlayan və onları lüğətə
    çevirən sinif.
    """

    def __init__(self, first_name, last_name, age):
        """
        Yeni bir Student obyekti yaradır.

        Arqumentlər:
            first_name (str): Tələbənin adı.
            last_name (str): Tələbənin soyadı.
            age (int): Tələbənin yaşı.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Student nümunəsinin lüğət (dictionary) təsvirini qaytarır.
        """
        return self.__dict__

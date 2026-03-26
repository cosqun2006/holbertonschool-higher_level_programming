#!/usr/bin/python3
"""BaseGeometry modulu üçün sənədləşdirmə"""


class BaseGeometry:
    """Həndəsi fiqurlar üçün baza sinfi"""

    def area(self):
        """Hələ ki tətbiq edilməmiş sahə hesablama metodu"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Tam ədədləri yoxlayan metod
        Args:
            name (str): Parametrin adı.
            value (int): Yoxlanılacaq dəyər.
        Raises:
            TypeError: value tam ədəd deyilsə.
            ValueError: value 0 və ya daha kiçikdirsə.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

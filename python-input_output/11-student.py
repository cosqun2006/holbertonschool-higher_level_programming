#!/usr/bin/python3
"""
Tələbə (Student) sinfini təyin edən modul.
"""


class Student:
    """
    Tələbə məlumatlarını saxlayan sinif.
    """

    def __init__(self, first_name, last_name, age):
        """Obyekti başladır"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Obyektin lüğətini qaytarır (Süzgəcləmə ilə).
        """
        # 1. Yoxlayırıq: attrs siyahıdır və içindəkilər stringdir?
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            yeni_luget = {}
            for acat in attrs:
                # Əgər obyektin daxilində (self.__dict__) belə bir açar varsa:
                if acat in self.__dict__:
                    yeni_luget[acat] = self.__dict__[acat]
            return yeni_luget

    def reload_from_json(self, json):
        """Lüğətdəki məlumatlarla obyektin bütün atributlarını yeniləyir."""
        for key, value in json.items():
            setattr(self, key, value)

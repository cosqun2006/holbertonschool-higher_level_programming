#!/usr/bin/python3
"""
Bu modul Python lüğətini (dictionary) JSON faylına
seriallaşdırmaq və yenidən geri oxumaq üçün funksiyaları ehtiva edir.
"""
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, mode='w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    with open(filename, mode='r', encoding="utf-8") as f:
        return json.load(f)

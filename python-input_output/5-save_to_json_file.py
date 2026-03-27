#!/usr/bin/python3
"""
Bu modul obyekti JSON formatında fayla yazan funksiyanı ehtiva edir
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Python obyektini JSON olaraq fayla qeyd edir
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)

#!/usr/bin/python3
"""
Bu modul JSON faylından obyekti yükləyən funksiyanı ehtiva edir
"""
import json


def load_from_json_file(filename):
    """
    JSON faylını oxuyur və Python obyektini qaytarır
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)

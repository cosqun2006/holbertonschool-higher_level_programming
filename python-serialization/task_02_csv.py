#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json:
    """
        CSV faylını oxuyur, hər sətri lüğətə (dict) çevirir
        və nəticəni JSON kimi saxlayır.
    """
    try:
        with open('csv_filename', mode='r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            data_list = [row for row in reader]
        with open('json.csv', mode='w', encoding="utf-8") as jsonfile:
            json.dump(data_list, jsonfile, indent=4)
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False

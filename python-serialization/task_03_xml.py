#!/usr/bin/env python3
"""
Bu modul Python lüğətini (dictionary) XML formatına çevirmək
və yenidən geri oxumaq üçün funksiyaları ehtiva edir.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Python lüğətini XML formatına çevirir və fayla yazır.
    """
    # 1. Kök element yaradırıq (məsələn: <data>)
    root = ET.Element("data")

    # 2. Lüğətin hər bir üzvünü kök elementə alt-element (child) kimi əlavə edirik
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # XML-də hər şey mətn kimi yadda qalır

    # 3. ElementTree obyekti yaradırıq və fayla yazırıq
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    XML faylını oxuyur və onu Python lüğətinə (dictionary) çevirir.
    """
    try:
        # 1. Faylı analiz (parse) edirik
        tree = ET.parse(filename)
        root = tree.getroot()

        # 2. XML elementlərini lüğətə yığırıq
        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text

        return deserialized_dict

    except FileNotFoundError:
        return None

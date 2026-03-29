import sys
import xml.etree.ElementTree as ET
from fileinput import filename


def serialize_to_xml(dictionary, filename):
    """
    Python lüğətini XML faylına yazır.

    Parametrlər:
    - dictionary: Python lüğəti
    - filename: XML fayl adı
    """

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml:
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        deserialed_dict = {}
        for child in root:
            deserialed_dict[child.tag] = child.text
        return deserialed_dict
    except FileNotFoundError:
        return None

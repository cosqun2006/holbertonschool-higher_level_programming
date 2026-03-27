#!/usr/bin/python3
"""
Module for Mixins and Dragon class
"""


def read_file(filename=""):
    with open(filename, "r") as file:
        print(file.read())

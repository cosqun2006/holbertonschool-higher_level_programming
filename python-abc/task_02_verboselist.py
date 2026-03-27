#!/usr/bin/python3
"""
Module for Shape abstract class and its subclasses
"""


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extend(self, iterable):
        counts = len(iterable)
        super().extend(iterable)
        print("Extended to the list with [{}] items".format(counts))

    def remove(self, item):
        print("Removing [{}] from the list".format(item))
        super().remove(self, item)

    def pop(self, index=- 1):
        item = self[index]
        print("Popped [{}] from the list".format(item))
        return super().pop(index)

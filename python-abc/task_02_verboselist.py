#!/usr/bin/python3
"""
Module for VerboseList class that extends the built-in list
"""


class VerboseList(list):
    """A list that prints notifications when modified"""

    def append(self, item):
        """Adds an item and prints a notification"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extends the list and prints how many items were added"""
        items_count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(items_count))

    def remove(self, item):
        """Prints notification before removing an item"""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Prints notification before popping an item"""
        # Siyahı boş deyilsə, çıxacaq elementi əvvəlcədən tapırıq
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)

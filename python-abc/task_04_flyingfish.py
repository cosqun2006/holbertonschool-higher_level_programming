#!/usr/bin/python3
"""
Module for Fish, Bird, and FlyingFish classes
Exploring Multiple Inheritance
"""


class Fish:
    """Parent class representing a fish"""
    def swim(self):
        """Standard swimming behavior"""
        print("The fish is swimming")

    def habitat(self):
        """Standard fish habitat"""
        print("The fish lives in water")


class Bird:
    """Parent class representing a bird"""
    def fly(self):
        """Standard flying behavior"""
        print("The bird is flying")

    def habitat(self):
        """Standard bird habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Subclass inheriting from both Fish and Bird"""
    def fly(self):
        """Override bird's fly method"""
        print("The flying fish is soaring!")

    def swim(self):
        """Override fish's swim method"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat method from both parents"""
        print("The flying fish lives both in water and the sky!")

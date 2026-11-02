#!/usr/bin/env python3
"""Module that defines a Square class with a getter and setter for size."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a square with an optional size."""
        self.size = size

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size, validating that it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

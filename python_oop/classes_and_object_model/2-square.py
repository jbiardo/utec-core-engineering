#!/usr/bin/env python3
"""Module that defines a Square class with a validated private size."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a square, validating that size is an int >= 0."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

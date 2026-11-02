#!/usr/bin/env python3
"""Module that defines a Square class with size, position and printing."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with an optional size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position, validating it is a tuple of 2 ints >= 0."""
        message = "position must be a tuple of 2 positive integer"
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(message)
        for number in value:
            if not isinstance(number, int) or number < 0:
                raise TypeError(message)
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the square drawn with # as a string."""
        if self.__size == 0:
            return ""
        lines = []
        for _ in range(self.__position[1]):
            lines.append("")
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(lines)

    def my_print(self):
        """Print the square with the # character."""
        print(self)

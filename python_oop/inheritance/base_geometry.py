#!/usr/bin/env python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """Base class with behavior shared by geometric shapes."""

    def area(self):
        """Raise an exception: area is not implemented in the base class."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

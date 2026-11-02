#!/usr/bin/env python3
"""Module that demonstrates inheritance and polymorphism with animals."""


class Animal:
    """Represent a generic animal."""

    def speak(self):
        """Return a generic animal sound."""
        return "Some sound"


class Dog(Animal):
    """Represent a dog, a kind of Animal."""

    def speak(self):
        """Return the sound of a dog."""
        return "Woof"


class Cat(Animal):
    """Represent a cat, a kind of Animal."""

    def speak(self):
        """Return the sound of a cat."""
        return "Meow"


def main():
    """Run the inheritance and polymorphism demo."""
    dog = Dog()
    cat = Cat()

    print(dog.speak())
    print(cat.speak())

    animals = [Dog(), Cat(), Dog()]
    for animal in animals:
        print(animal.speak())

    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(issubclass(Dog, Animal))


if __name__ == "__main__":
    main()

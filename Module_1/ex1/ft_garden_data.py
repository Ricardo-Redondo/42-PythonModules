#!/usr/bin/env python3

class Plant:
    """A class representing a plant with name, height, and age"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant with name, height, and age"""
        self.name = name
        self.height = height
        self.age = age


def main() -> None:
    """Adding 3 plants with different attributes then printing them"""
    plant1: Plant = Plant("rose", 1, 5)
    plant2: Plant = Plant("chocolate cosmos", 60, 12)
    plant3: Plant = Plant("black bat", 100, 30)
    print(f"{plant1.name}: {plant1.height} height, {plant1.age} days old")
    print(f"{plant2.name}: {plant2.height} height, {plant2.age} days old")
    print(f"{plant3.name}: {plant3.height} height, {plant3.age} days old")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

class Plant:
    """A class representing a plant with name, height, and age"""

    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant with name, height, and age"""
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        """Increase plant height by 5cm"""
        self.height += 5
        print(f"{self.name} has grown 5cm")

    def age(self) -> None:
        """Increase plant age by 1 day"""
        self.age = self.age + 1
        print(f"{self.name} has aged 1 day")

    def get_info(self) -> None:
        """Print plant information"""
        print(f"{self.name}: {self.height} cm, {self.age} days old\n")


def main() -> None:
    """Create plants, simulate growth over a week, and display results"""
    plant1: Plant = Plant("rose", 1, 5)
    plant2: Plant = Plant("chocolate cosmos", 60, 12)
    plant3: Plant = Plant("black bat", 100, 30)
    count: int = 0

    plants: list[Plant] = [plant1, plant2, plant3]
    print("Initial status:\n")
    for plant in plants:
        plant.get_info()

    Range: list[int] = [1, 2, 3, 4, 5, 6, 7]
    for i in Range:
        for plant in plants:
            plant.grow
            plant.age

    print("After a week\n")
    for plant in plants:
        plant.get_info()
        count += 5
    print(f"Growth this week: {count}")


if __name__ == "__main__":
    main()

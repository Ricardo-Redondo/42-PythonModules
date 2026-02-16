#!/usr/bin/env python3

class Plant:
    """A class representing a plant with name, height, and age"""

    def __init__(self, name: str, height: int, plant_age: int) -> None:
        """Initialize a plant with name, height, and age"""
        self.name: str = name
        self.height: int = height
        self.plant_age: int = plant_age

    def grow(self) -> None:
        """Increase plant height by 5cm"""
        self.height += 5

    def age(self) -> None:
        """Increase plant age by 1 day"""
        self.plant_age += 1

    def get_info(self) -> None:
        """Print plant information"""
        print(f"{self.name}: {self.height} cm, {self.plant_age} days old")


def main() -> None:
    """Create plants, simulate growth over a week, and display results"""
    plant1: Plant = Plant("rose", 1, 5)
    plant2: Plant = Plant("chocolate cosmos", 60, 12)
    plant3: Plant = Plant("black bat", 100, 30)
    count: int = 0

    plants: list[Plant] = [plant1, plant2, plant3]
    print("=== Day 1 ===")
    for plant in plants:
        plant.get_info()

    for i in range(1, 8):
        for plant in plants:
            plant.grow()
            plant.age()
            count += 5

    print("\n=== Day 7 ===")
    for plant in plants:
        plant.get_info()
    print(f"\nGrowth this week: {count}")


if __name__ == "__main__":
    main()

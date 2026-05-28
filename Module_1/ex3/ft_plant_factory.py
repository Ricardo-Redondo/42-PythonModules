#!/usr/bin/env python3

class Plant:
    """A class representing a plant with name, height, and age"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant with name, height, and age"""
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def get_info(self) -> None:
        """Print plant information"""
        print(f"{self.name}: {self.height} cm, {self.age} days old")


def main() -> None:
    """Create plants automatically and display their contents"""

    print("=== Plant Factory Output ===\n")

    plant_data: list[tuple[str, int, int]] = [
        ("rose", 1, 5),
        ("chocolate cosmos", 40, 12),
        ("black bat", 26, 29),
        ("flame lily", 20, 10),
        ("Ghost orchid", 16, 17)
    ]
    plants: list[Plant] = []

    for name, height, age in plant_data:
        plant: Plant = Plant(name, height, age)
        plants.append(plant)

    for plant in plants:
        plant.get_info()

    print(f"\nTotal plants: {len(plants)}")


if __name__ == "__main__":
    main()

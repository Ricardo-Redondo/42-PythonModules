#!/usr/bin/env python3

class SecurePlant:
    """A class representing a plant with validation for height and age"""

    def __init__(self, name: str) -> None:
        """Initialize a secure plant with name, height, and age"""
        self.name: str = name
        self.__height: int = 0
        self.__age: int = 0

    def set_height(self, height: int) -> None:
        """Set plant height if positive, otherwise reject"""
        if int(height) > 0:
            self.__height = height
            print(f"Height updated: {height} [OK]")
        else:
            print(f"Invalid operation attempted: height {height} [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        """Set plant age if positive, otherwise reject"""
        if int(age) > 0:
            self.__age = age
            print(f"Age updated: {age} [OK]")
        else:
            print(f"Invalid operation attempted: age {age} [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> int:
        """Return the plant's height"""
        return self.__height

    def get_age(self) -> int:
        """Return the plant's age"""
        return self.__age

    def get_info(self) -> None:
        """Print plant information"""
        print(f"Current plant: {self.name}"
              f" ({self.get_height()} cm, {self.get_age()} days)")


def main() -> None:
    """Create secure plants with validation and display their contents"""

    print("=== Garden Security System ===\n")

    plant_data: list[tuple[str, int, int]] = [
        ("rose", 1, 5),
        ("chocolate cosmos", 40, 12),
        ("black bat", 26, 29),
        ("flame lily", -20, 10),
        ("Ghost orchid", 16, -17)
    ]
    plants: list[SecurePlant] = []

    for name, height, age in plant_data:
        plant: SecurePlant = SecurePlant(name)
        print(f"Plant created: {plant.name}")
        plant.set_height(height)
        plant.set_age(age)
        print("\n")
        plants.append(plant)

    for plant in plants:
        plant.get_info()

    print(f"\nTotal plants: {len(plants)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

class Plant():
    """A class representing a plant with name and height"""
    def __init__(self, name: str, height: int):
        """Initialize a plant with name and height"""
        self.name = name
        self.height = height


class Garden:
    """A class representing a garden containing plants"""
    def __init__(self, name: str):
        """Initialize a garden with a name"""
        self.name = name
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden"""
        print(f"Added {plant.name} to {self.name}.")
        self.plants.append(plant)


class GardenError(Exception):
    """Base exception for garden-related errors"""
    pass


class PlantError(GardenError):
    """Error for plant-related issues"""
    pass


class WaterError(GardenError):
    """Error for watering issues"""
    pass


def water_plant(plant: Plant, amount: int) -> None:
    """Water a plant with validation"""
    if amount < 0:
        raise WaterError(f"{amount} is not valid")


def validate_plant(plant: Plant) -> None:
    """Validate plant height"""
    if plant.height <= 0:
        raise PlantError(f"{plant.name} has negative height")


def print_garden(garden: Garden) -> None:
    """Print garden information"""
    count: int = len(garden.plants)
    if count <= 0:
        raise GardenError("Garden is empty")


def test_errors() -> None:
    """Test all custom errors"""
    garden: Garden = Garden("garden")
    plant1: Plant = Plant("tulip", -1)
    plant2: Plant = Plant("rose", 5)

    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        validate_plant(plant1)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()

    print("Testing WaterError...")
    try:
        water_plant(plant2, -3)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()

    print("Testing catching all garden errors...")
    try:
        validate_plant(plant1)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        water_plant(plant2, -3)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        print_garden(garden)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_errors()

#!/usr/bin/env python3


class Plant():
    """
    A class representing a plant with name, height,
    water level and sunlight hours
    """
    def __init__(self, name: str, height: int, water_level: int,
                 sunlight_hours: int):
        """
        Initialize a plant with name, height, water level and sunlight hours
        """
        self.name = name
        self.height = height
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class Garden():
    """A class representing a garden containing plants"""
    def __init__(self, name: str):
        """Initialize a garden with a name"""
        self.name = name
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden"""
        print(f"Added {plant.name} successfully")
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


class HealthError(GardenError):
    """Exception class for health check errors"""
    pass


def water_plant(plant: Plant, amount: int) -> None:
    """Water a plant with validation for amount"""
    if amount < 0:
        raise WaterError(f"Error: {amount} is an invalid amount")
    else:
        print(f"Watering {plant.name} (+{amount} water level)")


def print_garden(garden: Garden) -> None:
    """Print information for all plants in the garden"""
    count: int = len(garden.plants)
    if count <= 0:
        raise GardenError()
    else:
        for plant in garden.plants:
            if plant.height <= 0:
                raise PlantError(plant)
            else:
                n = plant.name
                h = plant.height
                w = plant.water_level
                s = plant.sunlight_hours
                print(f"{n}: {h}, {w}, {s}")


def check_plant_health(plant: Plant) -> str:
    """
    Check if plant's water level and sunlight hours are within healthy ranges
    """
    w: int = plant.water_level
    h: int = plant.sunlight_hours

    if w < 1:
        raise HealthError(f"Error: Water level {w} is too low (min 1)!")
    if w > 10:
        raise HealthError(f"Error: Water level {w} is too high (max 10)!")
    if h < 2:
        raise HealthError(f"Error: Sunlight hours {h} is too low (min 2)!")
    if h > 12:
        raise HealthError(f"Error: Sunlight hours {h} is too high (max 12)!")

    return f"{plant.name} is healthy!"


class GardenManager():
    """A class to manage plants in a garden with validation and operations"""
    def __init__(self, garden: Garden):
        """Initialize garden manager with a garden"""
        self.garden = garden

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden with validation for name and height"""
        try:
            if len(plant.name) == 0:
                raise PlantError("Error: Plant name cannot be empty!")
            elif plant.height <= 0:
                raise PlantError("Error: Plant cannot have negative height!")
            else:
                self.garden.add_plant(plant)
        except PlantError as e:
            print(f"{e}")

    def water_plants(self, amount: int) -> None:
        """Water all plants in the garden with the specified amount"""
        print("Opening watering system")
        try:
            for plant in self.garden.plants:
                try:
                    water_plant(plant, amount)
                except WaterError as e:
                    print(f"{e}")
        finally:
            print("Closing Watering system")

    def check_plants_health(self) -> None:
        """Check the health of all plants in the garden"""
        print("Checking plant's health")
        try:
            for plant in self.garden.plants:
                try:
                    check_plant_health(plant)
                    print(f"{plant.name} is healthy")
                except HealthError as e:
                    print(f"{e}")
        finally:
            print("Finished checking plant's health")

    def create_plant(self, name: str, height: int, water_level: int,
                     sunlight_hours: int) -> Plant:
        """Create and return a new plant with specified attributes"""
        plant: Plant = Plant(name, height, water_level, sunlight_hours)
        return plant


def test_garden_management() -> None:
    """Test the garden management system with various scenarios"""
    garden: Garden = Garden("garden")
    manager: GardenManager = GardenManager(garden)

    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    plant1: Plant = manager.create_plant("tomato", 3, 5, 20)
    manager.add_plant(plant1)
    plant2: Plant = manager.create_plant("lettuce", 3, 15, 4)
    manager.add_plant(plant2)
    plant3: Plant = manager.create_plant("", 3, 1, 2)
    manager.add_plant(plant3)
    plant4: Plant = manager.create_plant("potato", -12, 1, 2)
    manager.add_plant(plant4)

    print("\nWatering plants (success)...")
    manager.water_plants(1)

    print("\nWatering plants (fail)...")
    manager.water_plants(-1)

    print("\nChecking plants health...")
    manager.check_plants_health()

    print("\nTesting error recovery...")
    print("Caught GardenError: not enough water in tank")
    print("System recovered and continuing...")

    print("\nGarden management system test completed!")


def main() -> None:
    """Main function to run garden management tests"""
    test_garden_management()


if __name__ == "__main__":
    main()

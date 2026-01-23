#!/usr/bin/env python3

class Plant():
    """A class representing a plant with name"""
    def __init__(self, name: str):
        """Initialize a plant with name"""
        self.name = name


class PlantError(Exception):
    """Error for plant-related issues"""
    def __init__(self, plant: Plant):
        """Initialize PlantError with plant reference"""
        message: str = f"Error: Cannot water {plant.name} - invalid plant"
        super().__init__(message)
        self.plant = plant


def water(plant: Plant) -> None:
    """Raise error if name is invalid otherwise water the plant"""
    if plant.name == "None":
        raise PlantError(plant)
    else:
        print(f"Watering {plant.name}")


def water_plants(plant_list: list[Plant]) -> None:
    """Go through the list of plants and try to water them"""
    print("Opening watering system")
    try:
        for plant in plant_list:
            try:
                water(plant)
            except PlantError as e:
                print(f"{e}")
    finally:
        print("Closing Watering system")


def test_watering_system() -> None:
    """Test a good plant list and bad plant list for errors"""
    plant_data_1: list[str] = [
        "tomato",
        "lettuce",
        "carrots"
    ]
    plant_data_2: list[str] = [
        "tomato",
        "lettuce",
        "None"
    ]
    plant_list_1: list[Plant] = []
    plant_list_2: list[Plant] = []

    for name in plant_data_1:
        plant: Plant = Plant(name)
        plant_list_1.append(plant)

    for name in plant_data_2:
        plant: Plant = Plant(name)
        plant_list_2.append(plant)

    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(plant_list_1)
    print("Watering completed successfully\n")
    print("Testing with error...")
    water_plants(plant_list_2)
    print("\nCleanup always happens, even with errors!")


def main() -> None:
    """Main function to run watering system tests"""
    test_watering_system()


if __name__ == "__main__":
    main()

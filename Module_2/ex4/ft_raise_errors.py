#!/usr/bin/env python3

class HealthError(Exception):
    """Exception class for health check errors"""
    pass


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """
    Check if plant health parameters are valid and within acceptable ranges
    """
    w = water_level
    s = sunlight_hours
    if len(plant_name) == 0:
        raise HealthError("Error: Plant name cannot be empty!")
    if w < 1:
        raise HealthError(f"Error: Water level {w} is too low (min 1)!")
    if w > 10:
        raise HealthError(f"Error: Water level {w} is too high (max 10)!")
    if s < 2:
        raise HealthError(f"Error: Sunlight hours {s} is too low (min 2)!")
    if s > 12:
        raise HealthError(f"Error: Sunlight hours {s} is too high (max 12)!")

    return f"Plant {plant_name} is healthy!"


def test_plant_checks() -> None:
    """Test error handling of plant health check arguments"""
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        print(f"{check_plant_health('tomato', 4, 7)}\n")
    except HealthError as e:
        print(f"{e}\n")

    print("Testing empty plant name...")
    try:
        print(f"{check_plant_health('', 4, 7)}\n")
    except HealthError as e:
        print(f"{e}\n")

    print("Testing bad water level...")
    try:
        print(f"{check_plant_health('tomato', 11, 7)}\n")
    except HealthError as e:
        print(f"{e}\n")

    print("Testing bad sunlight hours...")
    try:
        print(f"{check_plant_health('tomato', 4, 1)}\n")
    except HealthError as e:
        print(f"{e}\n")

    print("All error raising tests completed!")


def main() -> None:
    """Main function to run plant health check tests"""
    test_plant_checks()


if __name__ == "__main__":
    main()

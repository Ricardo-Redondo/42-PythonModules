#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int | None:
    """
    Check if temperature string is valid and within reasonable range (0-40)
    """
    try:
        num: int = int(temp_str)
        if 0 <= num <= 40:
            return num
        elif num < 0:
            print(f"Error: {num}°C is too cold for plants (min 0°C)")
        else:
            print(f"Error: {num}°C is too hot for plants (max 40°C)")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
    return None


def test_temperature_input() -> None:
    """Test temperature checking with various input values"""

    print("=== Garden Temperature Checker ===")

    test_values: list[str] = ["25", "abc", "100", "-50"]
    for temp in test_values:
        print(f"\nTesting temperature: {temp}")
        result: int | None = check_temperature(temp)
        if result is not None:
            print(f"Valid temperature: {result}")


if __name__ == "__main__":
    test_temperature_input()

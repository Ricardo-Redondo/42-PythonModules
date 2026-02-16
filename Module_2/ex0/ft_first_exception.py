#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int | None:
    """
    Check if temperature string is valid and within reasonable range (0-40)
    """
    try:
        num: int = int(temp_str)
        if 0 <= num <= 40:
            return num
        else:
            print("Not a reasonable temperature for plants")
    except ValueError:
        print("That is not a valid number")
    return None


def test_temperature_input() -> None:
    """Test temperature checking with various input values"""
    test_values: list[str] = ["25", "abc", "100", "-50"]
    for temp in test_values:
        result: int | None = check_temperature(temp)
        if result is not None:
            print(f"Valid temperature: {result}")


def main() -> None:
    """Run temperature input tests"""
    test_temperature_input()


if __name__ == "__main__":
    main()

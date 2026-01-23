#!/usr/bin/env python3

def garden_operations() -> None:
    """Demonstrates different types of errors"""

    # ValueError: converting bad input to int
    int("abc")

    # ZeroDivisionError: divide by zero
    result: int = 10 / 0
    result = result

    # FileNotFoundError: opening a file that doesn't exist
    file = open("missing.txt", "r")
    file.read()
    file.close()

    # KeyError: lookup missing key in dictionary
    garden: dict[str, int] = {"rose": 3, "tulip": 5}
    count: int = garden["_plant"]
    count = count


def test_error_types() -> None:
    """Test every error type and print when caught"""

    print("=== Garden Error Types Demo ===")

    print("Testing ValueError...\n")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: Invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        result: int = 10 / 0
        result = result
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        file = open("missing.txt", "r")
        file.read()
        file.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("Testing KeyError...")
    try:
        garden: dict[str, int] = {"rose": 3, "tulip": 5}
        count: int = garden["_plant"]
        count = count
    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")

    print("Testing multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


def main() -> None:
    """Run test_error_types"""
    test_error_types()


if __name__ == "__main__":
    main()

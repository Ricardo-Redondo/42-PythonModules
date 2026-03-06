#!/usr/bin/env python3

import sys


def main() -> None:
    """for more than 1 argument, iterates through them and prints them"""

    print("=== Command Quest ===\n")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()

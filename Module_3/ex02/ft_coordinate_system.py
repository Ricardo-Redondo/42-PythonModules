#!/usr/bin/env python3
import sys
import math


def calc_pos(pos1: tuple[int, int, int], pos2: tuple[int, int, int]) -> float:
    """Calculate 3D Euclidean distance between two positions"""
    distance: float = math.sqrt((pos2[0] - pos1[0])**2 +
                                (pos2[1] - pos1[1])**2 +
                                (pos2[2] - pos1[2])**2)
    return distance


def parse_coordinates(coord_str: str) -> tuple[int, int, int]:
    """Parse coordinate string into tuple of ints"""
    parts: list[str] = coord_str.split(',')
    x: int = int(parts[0])
    y: int = int(parts[1])
    z: int = int(parts[2])
    return (x, y, z)


def main() -> None:
    """Main function demonstrating 3D coordinate system"""
    print("=== Game Coordinate System ===")

    origin: tuple[int, int, int] = (0, 0, 0)
    pos1: tuple[int, int, int] = (10, 20, 5)
    print(f"Position created: {pos1}")

    distance_1: float = calc_pos(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {distance_1:.2f}")

    pos_str: str = "3,4,0"
    print(f"Parsing coordinates: \"{pos_str}\"")
    pos2: tuple[int, int, int] = parse_coordinates(pos_str)
    print(f"Parsed position: {pos2}")

    distance_2: float = calc_pos(origin, pos2)
    print(f"Distance between {origin} and {pos2}: {distance_2}")

    if len(sys.argv) == 2:
        pos_arg: str = sys.argv[1]
        print(f"Parsing coordinates: \"{pos_arg}\"")
        try:
            pos3: tuple[int, int, int] = parse_coordinates(pos_arg)
            print(f"Parsed position: {pos3}")
            distance_3: float = calc_pos(origin, pos3)
            print(f"Distance between {origin} and {pos3}: {distance_3}")
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    elif len(sys.argv) > 2:
        print("Too many arguments")
    else:
        print("no arguments were given")

    print("Unpacking demonstration:")
    x, y, z = pos2
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main() -> None:
    """strings variables that are printed"""
    name: str = "Chocolate cosmos"
    c_name: str = "Cosmos atrosanguineus"
    height: str = "40 to 60 cm tall"
    leaves_height: str = "7 to 15 cm long"

    print("Garden:")
    print(f"Flower name: {name}")
    print(f"Scientific name: {c_name}")
    print(f"Flower height: {height}")
    print(f"Leaves length: {leaves_height}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import alchemy.elements
from alchemy.potions import strength_potion
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water, create_earth


if __name__ == "__main__":
    print("=== Import Transmutation Mastery ===")

    print("\nMethod 1 - Full module import:")
    print(f"alchemy.elements.{alchemy.elements.create_fire.__name__}(): "
          f"{alchemy.elements.create_fire()} created")

    print("\nMethod 2 - Specific function import:")
    print(f"{create_water.__name__}(): {create_water()} created")

    print("\nMethod 3 - Aliased import:")
    print(f"{heal.__name__}(): {heal()} created")

    print("\nMethod 4 - Multiple import:")
    print(f"{create_earth.__name__}(): {create_earth()} created")
    print(f"{create_fire.__name__}(): {create_fire()} created")
    print(f"{strength_potion.__name__}(): {strength_potion()} created")

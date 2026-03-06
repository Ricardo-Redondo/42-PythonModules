#!/usr/bin/env python3

import alchemy

if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module acess: ")
    for i in [alchemy.elements.create_air,
              alchemy.elements.create_fire,
              alchemy.elements.create_earth,
              alchemy.elements.create_water]:
        print(f"alchemy.elements.{i.__name__}(): {i()} created")

    print("\nTesting package-level access (controlled by __init__.py):")
    for i in ["create_air", "create_fire", "create_earth", "create_water"]:
        try:
            func = getattr(alchemy, i)
            print(f"alchemy.{i}(): {func()} created")
        except AttributeError:
            print(f"alchemy.{i}(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__autour__}")

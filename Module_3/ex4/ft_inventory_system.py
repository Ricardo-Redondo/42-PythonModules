#!/usr/bin/env python3

import sys


def main() -> None:
    """
    Process inventory data passed via command arguments and print analytics.
    """
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}

    if len(sys.argv) == 1:
        print("No items in inventory!")
    else:
        for i in range(1, len(sys.argv)):
            item_arg: str = sys.argv[i]
            if ":" not in item_arg:
                continue
            key, val = item_arg.split(":", 1)
            inventory[key] = int(val)

        values: int = sum(inventory.values())
        print(f"Total items in inventory: {values}")

        items: int = len(inventory.keys())
        print(f"Unique item types: {items}")

        print("\n=== Current Inventory ===")
        for key, value in inventory.items():
            percentage: float = (value / values) * 100
            unit_label: str = "unit" if value == 1 else "units"
            print(f"{key}: {value} {unit_label} ({percentage:.1f}%)")

        print("\n=== Inventory Statistics ===")
        most: str = max(inventory, key=inventory.get)
        print(f"Most abundant: {most} ({inventory[most]} units)")
        least: str = min(inventory, key=inventory.get)
        print(f"Least abundant: {least} ({inventory[least]} units)")

        print("\n=== Item Categories ===")
        max_value: int = max(inventory.values())
        moderate_items: dict[str, int] = {}
        for key, value in inventory.items():
            if value == max_value:
                moderate_items[key] = value
        print(f"Moderate: {moderate_items}")

        scarce_items: dict[str, int] = {}
        for key, value in inventory.items():
            if value != max_value:
                scarce_items[key] = value
        print(f"Scarce: {scarce_items}")

        print("\n=== Management Suggestions ===")
        min_value: int = min(inventory.values())
        min_items: list[str] = []
        for key, value in inventory.items():
            if value == min_value:
                min_items.append(key)
        print(f"Restock needed: {min_items}")

        print("\n=== Dictionary Properties Demo ===")
        print(f"Dictionary keys: {list(inventory.keys())}")
        print(f"Dictionary values: {list(inventory.values())}")
        sample: bool = "sword" in inventory
        print(f"Sample lookup - 'sword' in inventory: {sample}")


if __name__ == "__main__":
    main()

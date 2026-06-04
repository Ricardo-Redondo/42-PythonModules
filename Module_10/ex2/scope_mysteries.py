#!/usr/bin/env python3

from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value) -> None:
        vault[key] = value

    def recall(key: str):
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":

    print("\n\033[33mTesting mage counter...\033[0m")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("Counter A:", end=" ")
    for i in range(1, 4):
        print(counter_a(), end=" ")
    print(f"\nCounter B: {counter_b()}")

    print("\n\033[33mTesting spell accumulator...\033[0m")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("\n\033[33mTesting enchantment factory...\033[0m")
    flame = enchantment_factory("Flaming")
    frost = enchantment_factory("Frozen")
    print(flame("Sword"))
    print(frost("Shield"))

    print("\n\033[33mTesting memory vault...\033[0m")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")

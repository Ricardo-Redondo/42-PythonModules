#!/usr/bin/env python3

from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    ops: dict[str, Callable[[int, int], int]] = {
        "add":      add,
        "multiply": mul,
        "max":      max,
        "min":      min,
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: '{operation}'")

    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire":  partial(base_enchantment, power=50, element="fire"),
        "ice":   partial(base_enchantment, power=50, element="ice"),
        "storm": partial(base_enchantment, power=50, element="storm"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell: Any) -> str:
        return f"Unknown spell type: '{spell}'"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":

    print("\n\033[33mTesting spell reducer...\033[0m")

    spells = [10, 20, 30, 40]
    for i in ["Add", "multiply", "Max", "Min", "Log", "Exp"]:
        try:
            print(f"{i}: {spell_reducer(spells, i.lower())}")
        except ValueError as e:
            print(e)

    print("\n\033[33mTesting partial enchanter...\033[0m")

    def base_enchantment(target: str, power: int, element: str) -> str:
        return (f"{element.capitalize()} enchantment on "
                f"{target} with power {power}")

    enchants = partial_enchanter(base_enchantment)
    print(enchants["fire"](target="Sword"))
    print(enchants["ice"](target="Shield"))
    print(enchants["storm"](target="Staff"))

    print("\n\033[33mTesting memoized fibonacci...\033[0m")

    for n in [0, 1, 10, 15]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\n\033[33mTesting spell dispatcher...\033[0m")

    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch([1, 2, 3]))
    print(dispatch(3.14))

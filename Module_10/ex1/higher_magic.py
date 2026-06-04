#!/usr/bin/env python3

from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[Callable, Callable]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplify_power(target: str, power: int) -> Callable:
        return base_spell(target, power * multiplier)
    return amplify_power


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cond_cast(target: str, power: int) -> Callable | str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return cond_cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def speller(target: str, power: int) -> list[Callable]:
        return [spell(target, power) for spell in spells]
    return speller


if __name__ == "__main__":

    def fireball(target: str, power: int):
        return f"Fireball hits {target} for {power} damage"

    def freeze(target: str, power: int):
        return f"Froze {target} for {power} damage"

    def lightning(target: str, power: int):
        return f"Lightning strikes {target} for {power} damage"

    print("\n\033[33mTesting spell_combiner...\033[0m")
    combo = spell_combiner(fireball, freeze)
    result = combo("dragon", 5)
    print(f"Combo result: {result[0]}, {result[1]}")

    print("\n\033[33mTesting power_amplifier...\033[0m")
    amplified_spell = power_amplifier(fireball, 3)
    print(f"Original spell:  {fireball('dragon', 5)}")
    print(f"Amplified spell: {amplified_spell('dragon', 5)}")

    print("\n\033[33mTesting conditional_caster...\033[0m")
    only_on_bosses = conditional_caster(
        lambda target, _: target in ("dragon", "lich"),
        fireball
    )
    print(only_on_bosses("dragon", 10))
    print(only_on_bosses("goblin", 10))

    print("\n\033[33mTesting spell_sequence...\033[0m")
    barrage = spell_sequence([fireball, freeze, lightning])
    for effect in barrage("troll", 4):
        print(effect)

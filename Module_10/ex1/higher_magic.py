#!usr/bin/venv python3

from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[any, any]:
        return (spell1(target, pow), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplify_power(target: str, power: int) -> any:
        return base_spell(target, power) * multiplier
    return amplify_power


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cond_cast(target: str, power: int) -> any:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return cond_cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def speller(target: str, power: int) -> any:
        return [spell(target, power) for spell in spells]
    return speller


if __name__ == "__main__":

    def fireball(target: str, power: int):
        return f"Fireball hits {target} for {power} damage"

    def freeze(target: str, power: int):
        return f"Froze {target} for {power} damage"

    print("\n\033[43mTesting spell combiner...\033[0m")

    combo = spell_combiner(fireball, freeze)
    combo("dragon", 5)

    print("\n\033[43mTesting power amplifier...\033[0m")
    amplified_spell = power_amplifier(fireball, 3)
    print(f"Original spell: {fireball("dragon", 5)}")
    print(f"amplified spell: {amplified_spell("dragon", 5)}")

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone():
    return (f"Philosopher’s stone created using {lead_to_gold()} "
            f"and {healing_potion()}")


def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"

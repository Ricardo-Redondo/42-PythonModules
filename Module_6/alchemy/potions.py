#!/usr/bin/env python3

from .elements import create_air, create_earth, create_fire, create_water


def healing_potion() -> str:
    return (f"Healing potion brewed with {create_fire()} "
            f"and {create_water()}")


def strength_potion() -> str:
    return (f"Strength potion brewed with {create_earth()} "
            f"and {create_fire()}")


def invisibility_potion() -> str:
    return (f"Invisibility potion brewed with {create_air()} "
            f"and {create_water()}")


def wisdom_potion() -> str:
    return (f"wisdom potion brewed with all elements: {create_air()}, "
            f"{create_fire()}, {create_earth()}, {create_water()}")

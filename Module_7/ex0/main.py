#!/usr/bin/env python3

from CreatureCard import CreatureCard


if __name__ == "__main__":
    print("\n=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:\n")
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    result = fire_dragon.play({"python": "bad"})
    print(f"Play result: {result}")

    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {fire_dragon.attack_target("Goblin Warrior")}")

    print("\nTesting insufficient mana (3 available):")
    fire_dragon.mana = 3
    fire_dragon.play({"womp": "womp"})

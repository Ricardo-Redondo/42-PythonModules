import alchemy
from alchemy.transmutation import lead_to_gold, stone_to_gem
from alchemy.transmutation import philosophers_stone, elixir_of_life

if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    print(f"{lead_to_gold.__name__}(): {lead_to_gold()}")
    print(f"{stone_to_gem.__name__}(): {stone_to_gem()}")

    print("\nTestint Relative Imports (from advanced.py):")
    print(f"{philosophers_stone.__name__}(): {philosophers_stone()}")
    print(f"{elixir_of_life.__name__}(): {elixir_of_life()}")

    print("\nTesting Package Access:")
    print(f"alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print(f"alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")

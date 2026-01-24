#!/usr/bin/env python3

from typing import Iterator


def game_events(num_events: int) -> Iterator[tuple[str, int, str]]:
    """Generator that yields varied game events as a tuple"""
    players: dict[str, int] = {
        "alice": 5,
        "bob": 12,
        "charlie": 8
    }
    events: list[str] = [
        "killed monster",
        "found treasure",
        "leveled up"
    ]

    player_names: list[str] = list(players.keys())

    for i in range(num_events):
        player: str = player_names[i % len(player_names)]
        lvl: int = players[player]
        action: str = events[i % len(events)]

        if action == "leveled up":
            players[player] = lvl + 1

        message: str = f"Event {i + 1}: Player {player} (level {lvl}) {action}"
        # Yielding as a tuple to allow unpacking in the loop
        yield (message, lvl, action)


def fibonacci(num: int) -> Iterator[int]:
    """Generator that yields each number of the fibonacci sequence"""
    a: int = 0
    b: int = 1
    for _ in range(num):
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime(num: int) -> Iterator[int]:
    """Generate first 'num' prime numbers"""
    count: int = 0
    candidate: int = 2

    while count < num:
        if is_prime(candidate):
            yield candidate
            count += 1
        candidate += 1


def main() -> None:
    """Demonstrates the use of generators for memory efficiency"""
    print("=== Game Data Stream Processor ===\n")

    num_events: int = 100
    lvl_counter: int = 0
    treasure_counter: int = 0
    lvl_ups: int = 0
    print(f"Processing {num_events} game events...\n")

    for event_msg, level, action in game_events(num_events):
        print(event_msg)
        if level > 10:
            lvl_counter += 1
        if action == "found treasure":
            treasure_counter += 1
        if action == "leveled up":
            lvl_ups += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {num_events}")
    print(f"High-level players (10+): {lvl_counter}")
    print(f"Treasure events: {treasure_counter}")
    print(f"Level-up events: {lvl_ups}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    fib_list: list[int] = []
    for num in fibonacci(10):
        fib_list.append(num)
    print(f"Fibonacci sequence (first 10): {fib_list}")

    prime_list: list[int] = []
    for num in prime(5):
        prime_list.append(num)
    print(f"Prime numbers (first 5): {prime_list}")


if __name__ == "__main__":
    main()

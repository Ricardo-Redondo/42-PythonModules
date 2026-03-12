#!/usr/bin/env python3

def main() -> None:
    """
    demonstrates the use of lists, tuples, dictionaries and sets
    """
    raw_scores: list[int] = [2300, 1800, 2150, 2050, 1500, 900]
    player_data: list[tuple[str, int, int]] = [
        ("alice", 2300, 5),
        ("bob", 1800, 3),
        ("charlie", 2150, 7),
        ("diana", 2050, 4)
    ]
    regions: list[str] = ["north", "east", "north", "central", "east"]

    print("=== Game Analytics Dashboard ===")

    high_scorers: list[str] = [p[0] for p in player_data if p[1] > 2000]
    doubled_scores: list[int] = [s * 2 for s in raw_scores[:4]]
    active_players: list[str] = [p[0] for p in player_data[:3]]

    print("\n=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {doubled_scores}")
    print(f"Active players: {active_players}")

    player_scores: dict[str, int] = {p[0]: p[1] for p in player_data}

    score_cats: dict[str, int] = {
        "high": len([s for s in raw_scores if s >= 2000]),
        "medium": len([s for s in raw_scores if 1000 <= s < 2000]),
        "low": len([s for s in raw_scores if s < 1000])
    }

    achievement_counts: dict[str, int] = {p[0]: p[2] for p in player_data}

    print("\n=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_cats}")
    print(f"Achievement counts: {achievement_counts}")

    unique_players: set[str] = {p[0] for p in player_data}
    unique_regions: set[str] = {r for r in regions}
    unique_achievements: set[str] = {"first_kill", "level_10", "boss_slayer"}

    print("\n=== Set Comprehension Examples ===")
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {unique_regions}")

    total_players: int = len(unique_players)
    avg_score: float = sum(raw_scores) / len(raw_scores)

    top_s: int = max([p[1] for p in player_data])
    top_p: list[tuple[str, int, int]] = [
        p for p in player_data if p[1] == top_s
    ]

    print("\n=== Combined Analysis ===")
    print(f"Total players: {total_players}")
    print("Total unique achievements: 12")
    print(f"Average score: {avg_score:.1f}")

    if top_p:
        name, score, ach = top_p[0]
        print(f"Top performer: {name} ({score} points, {ach} achievements)")


if __name__ == "__main__":
    main()

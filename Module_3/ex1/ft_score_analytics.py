#!/usr/bin/env python3

import sys


def main() -> None:
    """
    Adds every valid argument to the list scores and then,
    makes the following calculations
    """
    scores: list[int] = []
    print("=== Player Score Analytics ===\n")

    if len(sys.argv) == 1:
        print("No scores provided")
    else:
        for i in range(1, len(sys.argv)):
            try:
                scores.append(int(sys.argv[i]))
            except ValueError:
                print(f"{sys.argv[i]} is not a valid number")
        if len(scores) > 0:
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        else:
            print("There are no valid scores to analyze")


if __name__ == "__main__":
    main()

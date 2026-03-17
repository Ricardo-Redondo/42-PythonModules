#!/usr/bin/env python3
import sys


def main() -> None:
    """
    Demonstrate three-channel communication system with input,
    stdout, and stderr
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    a_id: str = input("Input stream active. Enter archivist ID: ")
    report: str = input("Input stream active. Enter status report: ")

    s: str = "[STANDARD] "
    a: str = "[ALERT] "

    sys.stdout.write(f"\n{s}Archive status from {a_id}: {report}\n")
    sys.stderr.write(f"{a}System diagnostics: Communication channels verified")
    sys.stderr.flush()  # Ensure stderr is displayed immediately
    sys.stdout.write(f"\n{s}Data transmission complete\n")

    print("\nThree-channel communication test successful\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3


def crisis_handler(filename: str) -> None:
    """Handle archive access with comprehensive error handling"""

    # Determine alert type based on filename
    if filename == "standard_archive.txt":
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        with open(filename, "r") as file:
            content = file.read().strip()

            # Check for corruption
            if "CORRUPTION" in content or "ERROR" in content:
                print(f"RESPONSE: Data corruption detected - {content}")
                print("STATUS: Crisis handled, data recovery attempted")
            else:
                print(f"SUCCESS: Archive recovered - '{content}'")
                print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception as e:
        print(f"RESPONSE: Unexpected anomaly - {e}")
        print("STATUS: Crisis handled, investigation required")


def main() -> None:
    """Test crisis response system with all scenarios"""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    # Test 1: File doesn't exist
    crisis_handler("lost_archive.txt")
    print()

    # Test 2: Permission error
    crisis_handler("classified_data.txt")
    print()

    # Test 3: Corrupted file (unexpected anomaly)
    crisis_handler("corrupted_archive.txt")
    print()

    # Test 4: Successful read
    crisis_handler("standard_archive.txt")
    print()

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()

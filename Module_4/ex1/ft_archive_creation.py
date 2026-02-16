#!/usr/bin/env python3

def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    try:
        print("\nInitializing new storage unit: new_discovery.txt")
        file = open("new_discovery.txt", "w")
        print("Storage unit created successfully...")

        lines: list[str] = [
            "[ENTRY 001] New quantum algorithm discovered\n",
            "[ENTRY 002] Efficiency increased by 347%\n",
            "[ENTRY 003] Archived by Data Archivist trainee"
        ]

        print("Inscribing preservation data...\n")
        for line in lines:
            file.write(line)
        print("[ENTRY 001] New quantum algorithm discovered")
        print("[ENTRY 002] Efficiency increased by 347%")
        print("[ENTRY 003] Archived by Data Archivist trainee")
        file.close()

        print("\nData inscription complete. Storage sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation")
    except PermissionError:
        print("ERROR: Permission denied - cannot create archive.")
    except OSError as e:
        print(f"ERROR: Archive creation failed - {e}")


if __name__ == "__main__":
    main()

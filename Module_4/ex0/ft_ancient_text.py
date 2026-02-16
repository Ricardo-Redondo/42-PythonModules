#!/usr/bin/env python3

def main() -> None:
    """Read and display ancient text fragments"""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("\nAccessing Storage Vault: ancient_fragment.txt")

    try:
        file = open("ancient_fragment.txt", "r")
        print("Connection established...")
        print("\nRECOVERED DATA:")

        content: str = file.read()
        print(content)

        print("\nData recovery complete. Storage unit disconnected")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main() -> None:
    """
    Using with:
    read from classified_data file and print,
    write from scurity_protocols to a new secure file
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nIniciating secure vault access...")
    print("Vault connection established with failsafe protocols")

    try:
        with open("classified_data.txt", "r") as file:
            print("\nSECURE EXTRACTION:")

            content: str = file.read()
            print(content)
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except PermissionError:
        print("ERROR: Permission denied - cannot open archive.")
    except OSError as e:
        print(f"ERROR: Archive opening failed - {e}")
    try:
        print("\nSECURE PRESERVATION:")
        with open("security_protocols.txt", "r") as file_1:
            file_1_content: list[str] = []
            for line in file_1.readlines():
                file_1_content.append(line)
            with open("secure_vault.txt", "w") as file_2:
                for line in file_1_content:
                    file_2.write(line)
                    print(line)

            print("Vault automatically sealed upon completion")
    except PermissionError:
        print("ERROR: Permission denied - cannot create archive.")
    except FileNotFoundError:
        print("ERROR: Security protocols not found. Run data generator first.")
    except OSError as e:
        print(f"ERROR: Archive creation failed - {e}")
    print("\nAll vault operations completed with maximum security\n")


if __name__ == "__main__":
    main()

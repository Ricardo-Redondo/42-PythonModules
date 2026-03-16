#!/usr/bin/env python3

import sys
import os
import site


if __name__ == "__main__":
    try:
        venv = sys.prefix != sys.base_prefix
        if not venv:
            print("\nMATRIX STATUS: You're still plugged in")
            print(f"\nCurrent Python: {sys.executable}")
            print("Virtual envorinment: None Detected")
            print("\nWARNING: You're in the global environment!")
            print("The machines can see everything you install.")
            print("\nTo enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate")
            print("\nThen run this program again.")
        else:
            print("\nMATRIX STATUS: Welcome to the construct")
            print(f"\nCurrent Python: {sys.executable}")
            print(f"Virtual envorinment: {os.path.basename(sys.prefix)}")
            print(f"Path to environment: {sys.prefix}")
            print("\nSUCCESS: You're in an isolated environment!"
                  "\nSafe to install packages without affecting"
                  "\nthe global system.")
            print("\nPackage installation path:")
            print(site.getusersitepackages())
    except Exception as e:
        print(e)

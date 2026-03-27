#!/usr/bin/env python3

import sys
import os
import site


if __name__ == "__main__":
    try:
        venv = sys.prefix != sys.base_prefix
        if not venv:
            print("\n\033[44mMATRIX STATUS: You're still plugged in\033[0m")

            print(f"\n\033[36mCurrent Python:\033[0m {sys.executable}")
            print("\033[36mVirtual environment:\033[0m None Detected")
            print("\n\033[5;43m[WARNING]\033[0m "
                  "You're in the global environment!")

            print("The machines can see everything you install.")

            print("\n\033[34mTo enter the construct, run:\033[0m")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate")

            print("\nThen run this program again.")
        else:
            print("\n\033[44mMATRIX STATUS: Welcome to the construct\033[0m")

            print(f"\n\033[36mCurrent Python:\033[0m {sys.executable}")
            print(f"\033[36mVirtual environment:\033[0m "
                  f"{os.path.basename(sys.prefix)}")

            print(f"\033[36mPath to environment:\033[0m {sys.prefix}")
            print("\n\033[5;42m[SUCCESS]\033[0m "
                  "You're in an isolated environment!")

            print("\nSafe to install packages without affecting "
                  "the global system.")

            print("\n\033[36mPackage installation path:\033[0m")
            print(site.getusersitepackages())
    except Exception as e:
        print(e)

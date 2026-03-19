#!/usr/bin/env python3

import sys
import importlib


def dependency_check(dependencies: list[str]) -> None:
    print("\nChecking dependencies:")
    for dependency in dependencies:
        error = 0
        try:
            package = importlib.import_module(dependency)
            if package is not None:
                if package.__name__ == "pandas":
                    print(f"\033[92m[OK]\033[0m {package.__name__} "
                          f"(\033[96m{package.__version__}\033[0m) ")
                elif package.__name__ == "requests":
                    print(f"\033[92m[OK]\033[0m {package.__name__} "
                          f"(\033[96m{package.__version__}\033[0m) ")
                elif package.__name__ == "matplotlib":
                    print(f"\033[92m[OK]\033[0m {package.__name__} "
                          f"(\033[96m{package.__version__}\033[0m) ")
                else:
                    print(f"\033[91m[ERROR]\033[0m {dependency} is not needed")
        except ImportError:
            error = 1
            print(f"\033[93m[MISSING]\033[0m {dependency}")
    if error == 1:
        print("\n" + "-" * 42)
        print("Try:")
        print("\033[92mpython3\033[96m -m\033[0m venv .venv")
        print("\033[92msource\033[95m .venv/bin/activate\033[0m")

        print("\nand:")

        print("\033[92mpython3\033[96m -m\033[0m pip "
              "install\033[96m -r\033[95m requirements.txt\033[0m")
        print("\033[92mpython3\033[95m loading.py\033[0m")

        print("\nor:")

        print("\033[92mpython3\033[96m -m\033[0m pip install poetry")
        print("\033[92mpoetry\033[0m install")
        print("\033[92mpoetry\033[0m run python\033[95m loading.py\033[0m")

        print("\nRun this program again.")
        print("-" * 42)


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...")
    dependency_check(["pandas", "requests", "matplotlib"])

    print("Analizing Matrix data...")

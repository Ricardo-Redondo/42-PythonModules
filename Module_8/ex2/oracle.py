#!/usr/bin/env python3
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    print("\n\033[33mORACLE STATUS:\033[0m Reading the Matrix...")
    try:
        load_dotenv()

        mode = os.getenv("MATRIX_MODE")
        url = os.getenv("DATABASE_URL")
        api_key = os.getenv("API_KEY")
        log_lvl = os.getenv("LOG_LEVEL")
        zion = os.getenv("ZION_ENDPOINT")

        missing = [name for name, val in {
            "MATRIX_MODE":    mode,
            "DATABASE_URL":   url,
            "API_KEY":        api_key,
            "LOG_LEVEL":      log_lvl,
            "ZION_ENDPOINT":  zion,
        }.items() if val is None or val == "None" or val.strip() == ""]

        if missing:
            raise ValueError(f"\033[5;41m[Error]\033[0m Missing variables: "
                             f"'{', '.join(missing)}'")

    except ValueError as e:
        print(str(e))
    except Exception as e:
        print(f"\033[41m[Error]\033[0m Unexpected error: {e}")
    else:
        print("\n\033[96mConfiguration loaded:\033[0m")
        print("\033[34mMODE:\033[0m", mode)
        print("\033[34mDATABASE_URL:\033[0m", url)
        print("\033[34mAPI_KEY:\033[0m", api_key)
        print("\033[34mLOG_LEVEL:\033[0m", log_lvl)
        print("\033[34mZION_ENDPOINT:\033[0m", zion)
        print("\n\033[42mORACLE STATUS:\033[0m "
              "Configuration loaded successfully.")

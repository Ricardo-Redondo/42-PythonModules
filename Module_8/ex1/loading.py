#!/usr/bin/env python3

import sys
import importlib


def dependency_check(dependencies: list[str]) -> None:
    print("\nChecking dependencies:")
    missing = []
    for dep in dependencies:
        try:
            pkg = importlib.import_module(dep)
            version = getattr(pkg, "__version__", "?.?.?")
            labels = {
                "pandas": "Data manipulation ready",
                "numpy": "Numerical engine ready",
                "requests": "Network access ready",
                "matplotlib": "Visualization ready",
            }
            print(f"\033[92m[OK]\033[0m {dep} (\033[96m{version}\033[0m) - ",
                  labels.get(dep, 'Ready'))
        except ImportError:
            missing.append(dep)
            print(f"\033[93m[MISSING]\033[0m {dep}")

    if missing:
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
        sys.exit(1)


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...")
    dependency_check(["pandas", "numpy", "requests", "matplotlib"])

    import requests
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nFetching Matrix data...")
    url = (
        "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
        "?vs_currency=usd&days=30&interval=daily"
    )
    try:
        resp = requests.get(url, timeout=10)

        resp.raise_for_status()
        # Raise an exception for HTTP errors

        raw_prices = resp.json()["prices"]
        # Grabs "prices" key from json response
        print(f"\033[92m[OK]\033[0m {len(raw_prices)} daily records received")
    except Exception as e:
        print(f"\033[5;93m[WARN]\033[0m API unavailable ({e}), "
              "using simulated data")
        np.random.seed(42)
        raw_prices = [
            [0, 60000 + i * 200 + np.random.normal(0, 1200)]
            for i in range(30)
        ]

    df = pd.DataFrame(raw_prices, columns=["timestamp_ms", "price"])
    # turns the list of [timestamp, price] pairs into a proper table

    df["date"] = pd.to_datetime(df["timestamp_ms"], unit="ms").dt.date
    # converts Unix milliseconds to human-readable dates

    df = df[["date", "price"]].copy()
    # keeps only the two useful columns
    # and makes a copy to avoid SettingWithCopyWarning

    prices = df["price"].to_numpy()
    # converts pandas column to raw numpy array

    mean = np.mean(prices)
    # average price over 30 days

    std = np.std(prices)
    # standard deviation (how much it deviates from the average)

    ma7 = np.convolve(prices, np.ones(7) / 7, mode="valid")
    # 7-day moving average (smooths out short-term fluctuations)

    print(f"Analyzing {len(prices)} data points...")
    print(f"  Mean  : ${mean:,.0f}")
    print(f"  Std   : ${std:,.0f}")
    print(f"  Range : ${prices.min():,.0f} - ${prices.max():,.0f}")

    BG, GREEN, CYAN, DIM = "#0d0d0d", "#00ff41", "#00e5ff", "#1a5c2e"

    fig, ax = plt.subplots(figsize=(10, 5), facecolor=BG)
    # creates the figure (the whole image) and ax (the axes/plot area)
    ax.set_facecolor(BG)

    x = np.arange(len(prices))
    x_ma7 = np.arange(6, len(prices))
    # 7-day moving average starts from the 7th day (index 6)

    ax.fill_between(x, prices, alpha=0.15, color=GREEN)
    #  shades the area under the price curve for better visibility

    ax.plot(x, prices, color=GREEN, lw=1.2, label="BTC/USD")
    #  plots the raw price data as a line

    ax.plot(x_ma7, ma7, color=CYAN,  lw=2.0, label="7-day avg")
    #  plots the 7-day moving average as a smoother line

    ax.axhline(mean, color=GREEN, lw=0.8, ls="--",
               alpha=0.5, label=f"Mean ${mean:,.0f}")
    #  adds a horizontal dashed line at the mean price for reference

    ax.set_title("BITCOIN · 30-DAY SIGNAL", color=GREEN,
                 fontfamily="monospace", fontsize=12, pad=10)
    #  sets the title of the plot with some styling

    ax.set_xlabel("Day", color=DIM, fontfamily="monospace")
    #  labels the x-axis as "Day" with styling

    ax.set_ylabel("Price (USD)", color=DIM, fontfamily="monospace")
    #  labels the y-axis as "Price (USD)" with styling

    ax.tick_params(colors=DIM, labelsize=8)
    #  styles the tick marks and labels on both axes

    for sp in ax.spines.values():
        sp.set_color(DIM)
        #  styles the borders of the plot area
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"${v:,.0f}"))
    #  formats the y-axis labels as currency (e.g., $60,000)

    ax.legend(facecolor=BG, edgecolor=DIM, labelcolor=GREEN,
              fontsize=8, prop={"family": "monospace"})
    #  adds a legend to the plot with styling

    plt.tight_layout()
    #  adjusts the layout to prevent clipping of labels and title

    plt.savefig("matrix_analysis.png", dpi=150,
                bbox_inches="tight", facecolor=BG)
    plt.close()

    print("\nGenerating visualization...")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")

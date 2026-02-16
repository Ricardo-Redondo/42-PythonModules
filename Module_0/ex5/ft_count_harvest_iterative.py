def ft_count_harvest_iterative() -> None:
    day_range: int = range(1, int(input("Days until harvest: ")) + 1)
    for i in day_range:
        print(f"Day {i}")
    print("Harvest time!")

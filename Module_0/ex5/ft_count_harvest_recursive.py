def ft_count_harvest_recursive(days: int = None) -> None:
    if days is None:
        days = int(input("Days until harvest: "))
        ft_count_harvest_recursive(days)
        print("Harvest time!")
        return
    if days > 0:
        ft_count_harvest_recursive(days - 1)
        print(f"Day {days}")

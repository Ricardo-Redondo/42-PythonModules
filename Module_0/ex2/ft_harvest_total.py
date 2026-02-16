def ft_harvest_total() -> None:
    day1: int = int(input("Day 1 harvest: "))
    day2: int = int(input("Day 2 harvest: "))
    day3: int = int(input("Day 3 harvest: "))
    total: int = day1 + day2 + day3
    print(f"Total harvest: {total}")

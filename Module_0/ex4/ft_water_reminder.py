def ft_water_reminder() -> None:
    water: int = int(input("Days since last watering: "))
    if water > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")

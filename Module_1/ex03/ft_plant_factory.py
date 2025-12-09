class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"{self.name}: {self.height} cm, {self.age} days old")


def main():
    plant_data = [
        ("rose", "0.45", "5"),
        ("chocolate cosmos", "40", "12"),
        ("black bat", "26", "29"),
        ("flame lily", "20", "10"),
        ("Ghost orchid", "16", "17")
    ]

    plants = []

    for name, height, age in plant_data:
        plant = Plant(name, height, age)
        plants.append(plant)

    for plant in plants:
        plant.get_info()

    print(f"\nTotal plants: {len(plants)}")


if __name__ == "__main__":
    main()

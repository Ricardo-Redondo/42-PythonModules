class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = 0
        self.__age = 0

    def set_height(self, height):
        if int(height) > 0:
            self.__height = height
            print(f"Height updated: {height} [OK]")
        else:
            print(f"Invalid operation attempted: height {height} [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age):
        if int(age) > 0:
            self.__age = age
            print(f"Age updated: {age} [OK]")
        else:
            print(f"Invalid operation attempted: age {age} [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def get_info(self):
        print(f"{self.name}:")
        print(f"\t{self.get_height()} cm,")
        print(f"\t{self.get_age()} days old.")


def main():
    plant_data = [
        ("rose", "1", "5"),
        ("chocolate cosmos", "40", "12"),
        ("black bat", "26", "29"),
        ("flame lily", "-20", "10"),
        ("Ghost orchid", "16", "-17")
    ]

    plants = []

    for name, height, age in plant_data:
        plant = SecurePlant(name, height, age)
        print(f"Plant created: {plant.name}")
        plant.set_height(height)
        plant.set_age(age)
        print("\n")
        plants.append(plant)

    for plant in plants:
        plant.get_info()

    print(f"\nTotal plants: {len(plants)}")


if __name__ == "__main__":
    main()

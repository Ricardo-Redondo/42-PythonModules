class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"{self.name}:")
        print(f"\t{self.get_height()} cm,")
        print(f"\t{self.get_age()} days old.")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.color} {self.name} is blooming!")

    def flower_info(self):
        self.get_info()
        print(f"\tand its color is {self.color}")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} with {self.trunk_diameter} has produced shade")

    def tree_info(self):
        self.get_info()
        print(f"\tand its trunk diameter is {self.trunk_diameter}")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def vegetable_info(self):
        self.get_info()
        print(f"\tits harvest season is {self.harvest_season},")
        print(f"\tand its rich in {self.nutritional_value}")


def main():
    flower_data = [
        ("rose", "1", "5", "red"),
        ("flame lily", "20", "10", "white")
    ]

    tree_data = [
        ("pine", "2000", "6000", "30"),
        ("oak", "800", "4000", "20")
    ]

    vegetable_data = [
        ("tomato", "40", "80", "summer", "vitamin C"),
        ("carrot", "60", "75", "fall", "vitamin K")
    ]

    plants = []

    for name, height, age, color in flower_data:
        plant = Flower(name, height, age, color)
        plants.append(plant)

    for name, height, age, trunk_diameter in tree_data:
        plant = Tree(name, height, age, trunk_diameter)
        plants.append(plant)

    for name, height, age, harvest_season, nutritional_value in vegetable_data:
        plant = Vegetable(name, height, age, harvest_season, nutritional_value)
        plants.append(plant)

    for plant in plants:
        if isinstance(plant, Flower):
            plant.flower_info()
            plant.bloom()
            print("\n")

        if isinstance(plant, Tree):
            plant.tree_info()
            plant.produce_shade()
            print("\n")

        if isinstance(plant, Vegetable):
            plant.vegetable_info()
            print("\n")


if __name__ == "__main__":
    main()

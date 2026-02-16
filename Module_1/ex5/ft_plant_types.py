#!/usr/bin/env python3

class Plant:
    """A base class representing a plant with name, height, and age"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant with name, height, and age"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_height(self) -> int:
        """Return the plant's height"""
        return self.height

    def get_age(self) -> int:
        """Return the plant's age"""
        return self.age

    def get_info(self) -> None:
        pass


class Flower(Plant):
    """A class representing a flower with color"""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a flower with name, height, age, and color"""
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """Display blooming message"""
        print(f"{self.color} {self.name} is blooming!")

    def get_info(self) -> None:
        """Print plant information"""
        print(f"{self.name.capitalize()} (Flower): {self.get_height()} cm, "
              f"{self.get_age()} days, {self.color} color")


class Tree(Plant):
    """A class representing a tree with trunk diameter"""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initialize a tree with name, height, age, and trunk diameter"""
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        """Display shade production message"""
        print(f"{self.name} with {self.trunk_diameter} has produced shade")

    def get_info(self) -> None:
        """Print plant information"""
        print(f"{self.name.capitalize()} (Tree): {self.get_height()} cm, "
              f"{self.get_age()} days, {self.trunk_diameter} cm diameter")


class Vegetable(Plant):
    """
    A class representing a vegetable with harvest season and nutritional value
    """

    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        """
        Initialize a vegetable with name, height, age,
        harvest season, and nutritional value
        """
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def get_info(self) -> None:
        """Print plant information"""
        print(f"{self.name.capitalize()} (Vegetable): {self.get_height()} cm, "
              f"{self.get_age()} days, {self.harvest_season},\n"
              f"{self.name.capitalize()} is rich in {self.nutritional_value}")


def main() -> None:
    """Create different types of plants and display their information"""

    print("=== Garden Plant Types ===\n")

    flower_data: list[tuple[str, int, int, str]] = [
        ("rose", 1, 5, "red"),
        ("flame lily", 20, 10, "white")
    ]
    tree_data: list[tuple[str, int, int, int]] = [
        ("pine", 2000, 6000, 30),
        ("oak", 800, 4000, 20)
    ]
    vegetable_data: list[tuple[str, int, int, str, str]] = [
        ("tomato", 40, 80, "summer", "vitamin C"),
        ("carrot", 60, 75, "fall", "vitamin K")
    ]
    plants: list[Plant] = []

    for name, height, age, color in flower_data:
        plant: Flower = Flower(name, height, age, color)
        plants.append(plant)

    for name, height, age, trunk_diameter in tree_data:
        plant: Tree = Tree(name, height, age, trunk_diameter)
        plants.append(plant)

    for name, height, age, harvest_season, nutritional_value in vegetable_data:
        plant: Vegetable = Vegetable(name, height, age,
                                     harvest_season, nutritional_value)
        plants.append(plant)

    for plant in plants:
        plant.get_info()
        if isinstance(plant, Flower):
            plant.bloom()
        elif isinstance(plant, Tree):
            plant.produce_shade()
        print() if plant != plants[-1] else None


if __name__ == "__main__":
    main()

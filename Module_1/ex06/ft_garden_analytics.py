class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, amount=0):
        self.height += amount
        print(f"{self.name} has grown {amount}cm.")
        return amount

    @staticmethod
    def validate_height(height):
        return height > 0

    def get_info(self):
        print(f"{self.name}: {self.height} cm.")


class FloweringPlant(Plant):
    def __init__(self, name, height, bloom):
        super().__init__(name, height)
        self.bloom = bloom


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, bloom, value):
        super().__init__(name, height, bloom)
        self.value = value


class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        print(f"Added {plant.name} to {self.name}.")
        self.plants.append(plant)


class GardenManager:
    def __init__(self):
        self.gardens = []
        self.stats = self.GardenStats(self)
        self.total_growth = 0
        self.total_plants = 0

    class GardenStats:
        def __init__(self, manager):
            self.manager = manager

        def count_plants(self):
            total = 0
            for garden in self.manager.gardens:
                total += len(garden.plants)
            return total

        def validate_all_heights(self):
            for garden in self.manager.gardens:
                for plant in garden.plants:
                    if not Plant.validate_height(plant.height):
                        return False
            return True

        def garden_scores(self):
            scores = []
            for garden in self.manager.gardens:
                total_score = 0

                for plant in garden.plants:
                    if isinstance(plant, PrizeFlower):
                        total_score += plant.value

                if "'" in garden.name:
                    owner = garden.name.split("'")[0]
                else:
                    owner = garden.name

                scores.append(f"{owner}: {total_score}")
            print(f"Garden scores - {', '.join(scores)}")

        def total_gardens(self):
            print(f"Total gardens managed: {len(self.manager.gardens)}")

        def count_by_type(self):
            r = 0
            f = 0
            p = 0

            for garden in self.manager.gardens:
                for plant in garden.plants:
                    if isinstance(plant, PrizeFlower):
                        p += 1
                    elif isinstance(plant, FloweringPlant):
                        f += 1
                    else:
                        r += 1
            print(f"Plants: {r} regular, {f} flowering, {p} prize flowers")

        def total_growth_and_plants(self):
            print(
                f"Plants added: {self.manager.total_plants}, "
                f"Total growth: {self.manager.total_growth}cm"
            )

    def add_garden(self, garden):
        self.gardens.append(garden)
        print(f"Added {garden.name} to the network.")

    def create_garden(self, name):
        new_garden = Garden(name)
        self.add_garden(new_garden)
        return new_garden

    def add_plant_to_garden(self, garden, plant):
        garden.add_plant(plant)
        self.total_plants += 1

    def grow_plant_in_garden(self, garden, plant_name, amount):
        for plant in garden.plants:
            if plant.name == plant_name:
                plant.grow(amount)
                self.total_growth += amount
                return
        print(f"Plant {plant_name} not found in {garden.name}")

    def generate_garden_report(self, garden):
        print(f"\n=== {garden.name} Report ===")
        print("Plants in garden:")
        for plant in garden.plants:
            info = f"- {plant.name}: {plant.height}cm"

            if isinstance(plant, FloweringPlant):
                if plant.bloom:
                    info += " (blooming)"

            if isinstance(plant, PrizeFlower):
                info += f", Prize points: {plant.value}"

            print(info)

    @classmethod
    def create_garden_network(cls):
        return cls()


def main():
    # Create manager using class method
    manager = GardenManager.create_garden_network()

    # Create gardens
    garden1 = manager.create_garden("Alice's garden")
    garden2 = manager.create_garden("Bob's garden")

    # Add plants to Alice's garden
    manager.add_plant_to_garden(
        garden1,
        Plant("Oak Tree", 100)
    )
    manager.add_plant_to_garden(
        garden1,
        FloweringPlant("Rose", 25, True)
    )
    manager.add_plant_to_garden(
        garden1,
        PrizeFlower("Sunflower", 50, True, 10)
    )

    # Add plants to Bob's garden
    manager.add_plant_to_garden(
        garden2,
        Plant("Cactus", 15)
    )
    manager.add_plant_to_garden(
        garden2,
        PrizeFlower("Prize Tomato", 30, True, 92)
    )

    # Make plants grow
    print("\nAlice is helping all plants grow...")
    manager.grow_plant_in_garden(garden1, "Oak Tree", 1)
    manager.grow_plant_in_garden(garden1, "Rose", 1)
    manager.grow_plant_in_garden(garden1, "Sunflower", 1)

    # Generate garden reports
    manager.generate_garden_report(garden1)
    manager.generate_garden_report(garden2)

    # Display statistics
    print()
    manager.stats.total_growth_and_plants()
    manager.stats.count_by_type()
    print(f"Height validation test: {manager.stats.validate_all_heights()}")
    manager.stats.garden_scores()
    manager.stats.total_gardens()


if __name__ == "__main__":
    main()

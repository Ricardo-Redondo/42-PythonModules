#!/usr/bin/env python3

class Plant:
    """A base class representing a plant with name and height"""

    def __init__(self, name: str, height: int) -> None:
        """Initialize a plant with name and height"""
        self.name: str = name
        self.height: int = height

    def grow(self, amount: int = 0) -> int:
        """Grow the plant by the specified amount"""
        self.height += amount
        print(f"{self.name} has grown {amount}cm.")
        return amount

    @staticmethod
    def validate_height(height: int) -> bool:
        """Validate that height is positive"""
        return height > 0

    def get_info(self) -> None:
        """Print plant information"""
        print(f"{self.name}: {self.height} cm.")


class FloweringPlant(Plant):
    """A class representing a flowering plant"""

    def __init__(self, name: str, height: int, bloom: bool) -> None:
        """Initialize a flowering plant with name, height, and bloom status"""
        super().__init__(name, height)
        self.bloom: bool = bloom


class PrizeFlower(FloweringPlant):
    """A class representing a prize-winning flower with point value"""

    def __init__(self, name: str, height: int, bloom: bool,
                 value: int) -> None:
        """
        Initialize a prize flower with name, height, bloom status, and value
        """
        super().__init__(name, height, bloom)
        self.value: int = value


class Garden:
    """A class representing a garden containing plants"""

    def __init__(self, name: str) -> None:
        """Initialize a garden with a name"""
        self.name: str = name
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden"""
        print(f"Added {plant.name} to {self.name}.")
        self.plants.append(plant)


class GardenManager:
    """A class managing multiple gardens and their statistics"""

    def __init__(self) -> None:
        """Initialize a garden manager"""
        self.gardens: list[Garden] = []
        self.stats: GardenManager.GardenStats = self.GardenStats(self)
        self.total_growth: int = 0
        self.total_plants: int = 0

    class GardenStats:
        """A nested class for managing garden statistics"""

        def __init__(self, manager: 'GardenManager') -> None:
            """Initialize garden stats with a reference to the manager"""
            self.manager: GardenManager = manager

        def count_plants(self) -> int:
            """Count total number of plants across all gardens"""
            total: int = 0
            for garden in self.manager.gardens:
                total += len(garden.plants)
            return total

        def validate_all_heights(self) -> bool:
            """Validate that all plants have positive heights"""
            for garden in self.manager.gardens:
                for plant in garden.plants:
                    if not Plant.validate_height(plant.height):
                        return False
            return True

        def garden_scores(self) -> None:
            """Print scores for each garden based on prize flowers"""
            scores: list[str] = []
            for garden in self.manager.gardens:
                total_score: int = 0

                for plant in garden.plants:
                    if isinstance(plant, PrizeFlower):
                        total_score += plant.value

                if "'" in garden.name:
                    owner: str = garden.name.split("'")[0]
                else:
                    owner: str = garden.name

                scores.append(f"{owner}: {total_score}")
            print(f"Garden scores - {', '.join(scores)}")

        def total_gardens(self) -> None:
            """Print total number of gardens managed"""
            print(f"Total gardens managed: {len(self.manager.gardens)}")

        def count_by_type(self) -> None:
            """Count and print plants by type"""
            r: int = 0
            f: int = 0
            p: int = 0

            for garden in self.manager.gardens:
                for plant in garden.plants:
                    if isinstance(plant, PrizeFlower):
                        p += 1
                    elif isinstance(plant, FloweringPlant):
                        f += 1
                    else:
                        r += 1
            print(f"Plants: {r} regular, {f} flowering, {p} prize flowers")

        def total_growth_and_plants(self) -> None:
            """Print total plants added and total growth"""
            print(
                f"Plants added: {self.manager.total_plants}, "
                f"Total growth: {self.manager.total_growth}cm"
            )

    def add_garden(self, garden: Garden) -> None:
        """Add a garden to the network"""
        self.gardens.append(garden)
        print(f"Added {garden.name} to the network.")

    def create_garden(self, name: str) -> Garden:
        """Create a new garden and add it to the network"""
        new_garden: Garden = Garden(name)
        self.add_garden(new_garden)
        return new_garden

    def add_plant_to_garden(self, garden: Garden, plant: Plant) -> None:
        """Add a plant to a specific garden"""
        garden.add_plant(plant)
        self.total_plants += 1

    def grow_plant_in_garden(self, garden: Garden, plant_name: str,
                             amount: int) -> None:
        """Grow a specific plant in a garden by the given amount"""
        for plant in garden.plants:
            if plant.name == plant_name:
                plant.grow(amount)
                self.total_growth += amount
                return
        print(f"Plant {plant_name} not found in {garden.name}")

    def generate_garden_report(self, garden: Garden) -> None:
        """Generate and print a detailed report for a garden"""
        print(f"\n=== {garden.name} Report ===")
        print("Plants in garden:")
        for plant in garden.plants:
            info: str = f"- {plant.name}: {plant.height}cm"

            if isinstance(plant, FloweringPlant):
                if plant.bloom:
                    info += " (blooming)"

            if isinstance(plant, PrizeFlower):
                info += f", Prize points: {plant.value}"

            print(info)

    @classmethod
    def create_garden_network(cls) -> 'GardenManager':
        """Create a new garden manager using a class method"""
        return cls()


def main() -> None:
    """Main function to demonstrate garden management system"""

    # Create manager using class method
    manager: GardenManager = GardenManager.create_garden_network()

    # Create gardens
    garden1: Garden = manager.create_garden("Alice's garden")
    garden2: Garden = manager.create_garden("Bob's garden")

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

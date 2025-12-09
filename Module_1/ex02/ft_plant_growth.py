class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 5
        print(f"{self.name} has grown 5cm")

    def age(self):
        self.age = self.age + 1
        print(f"{self.name} has aged 1 day")

    def get_info(self):
        print(f"{self.name}: {self.height} cm, {self.age} days old\n")


def main():
    plant1 = Plant("rose", "0.45", "5")
    plant2 = Plant("chocolate cosmos", "60", "12")
    plant3 = Plant("black bat", "100", "30")
    count = 0

    plants = [plant1, plant2, plant3]
    print("Initial status:\n")
    for plant in plants:
        plant.get_info()

    Range = [1, 2, 3, 4, 5, 6, 7]
    for i in Range:
        for plant in plants:
            plant.grow
            plant.age

    print("After a week\n")
    for plant in plants:
        plant.get_info()
        count += 5
    print(f"Growth this week: {count}")


if __name__ == "__main__":
    main()

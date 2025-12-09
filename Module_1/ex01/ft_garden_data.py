class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


def main():
    plant1 = Plant("rose", "0.45cm", "5")
    plant2 = Plant("chocolate cosmos", "60cm", "12")
    plant3 = Plant("black bat", "100cm", "30")
    print(f"{plant1.name}: {plant1.height} height, {plant1.age} days old")
    print(f"{plant2.name}: {plant2.height} height, {plant2.age} days old")
    print(f"{plant3.name}: {plant3.height} height, {plant3.age} days old")


if __name__ == "__main__":
    main()

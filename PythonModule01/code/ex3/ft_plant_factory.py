class Plant:
    def __init__(self, name: str, height: float, age_of_plant: int) -> None:
        self.name = name
        self.height = height
        self.age_of_plant = age_of_plant

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_of_plant} days old")

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 2)

    def age(self) -> None:
        self.age_of_plant += 1

    def creation_log(self) -> None:
        print("Created: ", end="")
        self.show()


if __name__ == "__main__":
    garden_data = [
        ("Rose", 25.0, 30),
        ("Oak", 200.0, 365),
        ("Cactus", 5.0, 90),
        ("Sunflower", 80.0, 45),
        ("Fern", 15.0, 120)
        ]
    plants = []

    print("=== Plant Factory Output ===")

    for data in garden_data:
        plant = Plant(*data)
        plant.creation_log()
        plant.grow()

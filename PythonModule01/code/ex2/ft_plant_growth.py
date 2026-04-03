class Plant:
    def __init__(self, name: str, height: float, age_of_plant: int) -> None:
        self.name = name
        self.height = height
        self.age_of_plant = age_of_plant

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_of_plant} days old")

    def grow(self, growth_rate: float = 0.8) -> None:
        self.height = round(self.height + growth_rate, 2)

    def age(self) -> None:
        self.age_of_plant += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    garden_plant = Plant("Rose", 25.0, 30)

    initial_heights = garden_plant.height

    for day in range(7):
        print(f"=== Day {day + 1} ===")
        garden_plant.show()
        garden_plant.grow()
        garden_plant.age()

    growth = round(garden_plant.height - initial_heights)
    print(f"Growth this week: {growth}cm")

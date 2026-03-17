class Plant:
    def __init__(self, name: str, height: int, age_of_plant: int) -> None:
        self.name = name
        self.height = height
        self.age_of_plant = age_of_plant

    def creation_log(self) -> None:
        print(
            f"""Created: {self.name} """
            f"""({self.height}cm, {self.age_of_plant} days)"""
            )


if __name__ == "__main__":
    garden_data = [("Rose", 25, 30), ("Oak", 200, 365), ("Cactus", 5, 90),
                   ("Sunflower", 80, 45), ("Fern", 15, 120)]
    plants = []

    print("=== Plant Factory Output ===")

    for data in garden_data:
        plants.append(Plant(*data))

    for plant in plants:
        plant.creation_log()

    print(f"\nTotal plants created: {len(plants)}")

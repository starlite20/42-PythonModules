class Plant:
    def __init__(self, name: str, height: int, age_of_plant: int):
        self.name = name
        self.height = height
        self.age_of_plant = age_of_plant

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age_of_plant} days old"

    def grow(self):
        self.height += 1

    def age(self):
        self.age_of_plant += 1


if __name__ == "__main__":
    garden = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    initial_heights = []
    for plant in garden:
        initial_heights.append(plant.height)

    print("=== Day 1 ===")
    for plant in garden:
        print(plant.get_info())

    for day in range(6):
        for plant in garden:
            plant.grow()
            plant.age()

    print("=== Day 7 ===")
    for plant in garden:
        print(plant.get_info())

    growth = garden[0].height - initial_heights[0]
    print(f"Growth this week: +{growth}cm")

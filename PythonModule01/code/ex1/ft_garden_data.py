class Plant:
    def __init__(self, name: str, height: int, age_of_plant: int):
        self.name = name
        self.height = height
        self.age_of_plant = age_of_plant

    def print_plant(self):
        print(f"{self.name}: {self.height}cm, {self.age_of_plant} days old")


if __name__ == "__main__":
    garden = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    print("=== Garden Plant Registry ===")
    for i in range(len(garden)):
        garden[i].print_plant()

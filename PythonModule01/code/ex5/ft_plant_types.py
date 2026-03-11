class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.type_name = "Plant"

    def get_base_info(self) -> str:
        return (
            f"""\n{self.name} ({self.type_name}): """
            f"""{self.height}cm, {self.age} days""")

    def update_plant_type(self, new_type_name: str) -> None:
        self.type_name = new_type_name


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.update_plant_type("Flower")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def display(self):
        print(f"{self.get_base_info()}, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk: int) -> None:
        super().__init__(name, height, age)
        self.trunk = trunk
        self.update_plant_type("Tree")

    def produce_shade(self):
        shade_area = self.trunk * 1.58
        print(f"{self.name} provides {shade_area:.0f} square meters of shade")

    def display(self):
        print(f"{self.get_base_info()}, {self.trunk}cm diameter")


class Vegetable(Plant):
    def __init__(
            self, name: str, height: int, age: int, harvest: str, nutri: str
            ) -> None:
        super().__init__(name, height, age)
        self.harvest = harvest
        self.nutri = nutri
        self.update_plant_type("Vegetable")

    def nutrition_value(self):
        print(f"{self.name} is rich in {self.nutri}")

    def display(self):
        print(f"{self.get_base_info()}, {self.harvest} harvest")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    garden = [
        Flower("Rose", 25, 30, "red"),
        Flower("Jasmine", 15, 10, "white"),
        Tree("Oak", 500, 1825, 50),
        Tree("Mango", 600, 2100, 60),
        Vegetable("Tomato", 80, 90, "summer", "Vitamin C"),
        Vegetable("Carrot", 15, 60, "winter", "Vitamin A")
    ]

    for i in range(len(garden)):
        plant = garden[i]
        plant.display()

        if plant.type_name == "Flower":
            plant.bloom()
        elif plant.type_name == "Tree":
            plant.produce_shade()
        elif plant.type_name == "Vegetable":
            plant.nutrition_value()

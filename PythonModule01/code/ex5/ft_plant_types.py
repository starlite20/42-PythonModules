class Plant:
    def __init__(self, name: str, height: float = 0.0, age_of_plant: int = 0) -> None:
        self.name = name
        self._height = height if height >= 0 else 0.0
        self._age_of_plant = age_of_plant if age_of_plant >= 0 else 0

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age_of_plant} days old")

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 2)

    def age(self) -> None:
        self._age_of_plant += 1

    def creation_log(self) -> None:
        print("Created: ", end="")
        self.show()

    def set_height(self, height_passed) -> None:
        if (height_passed < 0):
            print("Error, height can't be negative\nHeight update rejected")
        else:
            self._height = height_passed
            print(f"Height updated: {round(self._height,1)}cm")

    def set_age(self, age_passed) -> None:
        if (age_passed < 0):
            print("Error, age can't be negative\nAge update rejected")
        else:
            self._age_of_plant = age_passed
            print(f"Age updated: {self._age_of_plant} days")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> float:
        return (self._age_of_plant)

    def current_state(self) -> None:
        print("\nCurrent state: ", end="")
        self.show()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.update_plant_type("Flower")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def display(self) -> None:
        print(f"{self.get_base_info()}, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk: int) -> None:
        super().__init__(name, height, age)
        self.trunk = trunk
        self.update_plant_type("Tree")

    def produce_shade(self) -> None:
        shade_area = self.trunk * 1.58
        print(f"{self.name} provides {shade_area:.0f} square meters of shade")

    def display(self) -> None:
        print(f"{self.get_base_info()}, {self.trunk}cm diameter")


class Vegetable(Plant):
    def __init__(
            self, name: str, height: float, age: int, harvest: str, nutri: str
            ) -> None:
        super().__init__(name, height, age)
        self.harvest = harvest
        self.nutri = nutri
        self.update_plant_type("Vegetable")

    def nutrition_value(self) -> None:
        print(f"{self.name} is rich in {self.nutri}")

    def display(self) -> None:
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

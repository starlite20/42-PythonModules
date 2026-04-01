class Plant:
    def __init__(self, name: str, height: float = 0.0, age_of_plant: int = 0) -> None:
        self.name = name
        self._height = height if height >= 0 else 0.0
        self._age_of_plant = age_of_plant if age_of_plant >= 0 else 0
        self.type_name = "Plant"

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age_of_plant} days old")

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 2)

    def age(self) -> None:
        self._age_of_plant += 1

    def creation_log(self) -> None:
        print(f"=== {self.type_name}")
        self.show()

    def show_type(self) -> None:
        print(f"=== {self.type_name}")

    def update_plant_type(self, type_name: str) -> None:
        self.type_name = type_name

    def set_height(self, height_passed) -> None:
        if (height_passed < 0):
            print("Error, height can't be negative\nHeight update rejected")
        else:
            self._height = height_passed
            print(f"Height updated: {round(self._height, 1)}cm")

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

    def show(self) -> None:
        print(f"{self.get_base_info()}, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.update_plant_type("Tree")

    def produce_shade(self) -> None:
        shade_area = self.trunk_diameter * 1.58
        print(f"{self.name} provides {shade_area:.0f} square meters of shade")

    def show(self) -> None:
        print(f"{self.get_base_info()}, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self.update_plant_type("Vegetable")

    def nutritional_valuetion_value(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")

    def show(self) -> None:
        print(f"{self.get_base_info()}, {self.harvest_season} harvest_season")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    flower = Flower("Rose", 25, 30, "red")
    flower.creation_log()

    tree = Tree("Oak", 500, 1825, 50)
    tree.show_type()

    vegetable = Vegetable("Tomato", 80, 90, "summer", "Vitamin C")
    vegetable.show_type()

    for i in range(len(garden)):
        plant = garden[i]
        plant.show()

        if plant.type_name == "Flower":
            plant.bloom()
        elif plant.type_name == "Tree":
            plant.produce_shade()
        elif plant.type_name == "Vegetable":
            plant.nutritional_valuetion_value()

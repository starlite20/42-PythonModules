class Plant:
    def __init__(self, name: str, height: float = 0.0,
                 age_of_plant: int = 0) -> None:
        self.name = name
        self._height = height if height >= 0 else 0.0
        self._age_of_plant = age_of_plant if age_of_plant >= 0 else 0
        self.type_name = "Plant"

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self._height}cm, {self._age_of_plant} days old"
            )

    def grow(self) -> None:
        self._height = round(self._height + 2.1, 2)

    def age(self) -> None:
        self._age_of_plant += 1

    def show_type(self) -> None:
        print(f"=== {self.type_name}")

    def creation_log(self) -> None:
        self.show_type()
        self.show()

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
        self.bloom_state = False

    def bloom(self) -> None:
        self.bloom_state = True

    def show_bloom_state(self) -> None:
        if self.bloom_state:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        self.show_bloom_state()


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.update_plant_type("Tree")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name.capitalize()}"
            f" now produces a shade of {self.get_height()}cm long"
            f" and {self.trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self.update_plant_type("Vegetable")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def grow_and_age(self, age_for: int) -> None:
        for i in range(age_for):
            self.grow()
            self.age()

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    flower = Flower("rose", 15.0, 10, "red")
    flower.creation_log()
    print(f"[asking the {flower.name} to bloom]")
    flower.bloom()
    flower.show()

    print("\n", end="")
    tree = Tree("oak", 200.0, 365, 5.0)
    tree.creation_log()
    print(f"[asking the {tree.name} to produce shade]")
    tree.produce_shade()

    print("\n", end="")
    vegetable = Vegetable("tomato", 5.0, 10, "April", 0)
    vegetable.creation_log()
    age_for = 20
    print(f"[make {vegetable.name} grow and age for {age_for} days]")
    vegetable.grow_and_age(20)
    vegetable.show()

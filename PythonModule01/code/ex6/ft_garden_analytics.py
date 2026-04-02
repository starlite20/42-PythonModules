class Plant:
    class InternalStats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def increment_grow_calls(self) -> None:
            self._grow_calls += 1

        def increment_age_calls(self) -> None:
            self._age_calls += 1

        def increment_show_calls(self) -> None:
            self._show_calls += 1

        def get_grow_calls_count(self) -> int:
            return self._grow_calls

        def get_age_calls_count(self) -> int:
            return self._age_calls

        def get_show_calls_count(self) -> int:
            return self._show_calls

    def __init__(self, name: str = "Unknown plant", height: float = 0.0,
                 age_of_plant: int = 0) -> None:
        self.name = name
        self._height = height if height >= 0 else 0.0
        self._age_of_plant = age_of_plant if age_of_plant >= 0 else 0
        self.type_name = "Anonymous"
        self.stats = self.InternalStats()

    def show(self) -> None:
        self.stats.increment_show_calls()
        print(f"{self.name.capitalize()}: "
              f"{self._height}cm, {self._age_of_plant} days old")

    def grow(self, growth_rate: float = 8.0) -> None:
        self.stats.increment_grow_calls()
        self._height = round(self._height + growth_rate, 2)

    def age(self, age_rate: int = 1) -> None:
        self.stats.increment_age_calls()
        self._age_of_plant += age_rate

    def show_type(self) -> None:
        print(f"=== {self.type_name}")

    def show_statistics(self) -> None:
        print(
            f"Stats: {self.stats.get_grow_calls_count()} grow,"
            f" {self.stats.get_age_calls_count()} age,"
            f" {self.stats.get_show_calls_count()} show"
        )

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

    @staticmethod
    def older_than_a_year(age_value) -> bool:
        return age_value > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


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
        self.number_of_produced_shades = 0

    def produce_shade(self) -> None:
        self.number_of_produced_shades += 1
        print(
            f"Tree {self.name.capitalize()} "
            f"now produces a shade of {self.get_height()}cm"
            f" long and {self.trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def show_statistics(self) -> None:
        super().show_statistics()
        print(f" {self.number_of_produced_shades} shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self.update_plant_type("Vegetable")

    def grow(self, growth_rate: float = 8.0) -> None:
        super().grow(growth_rate)
        self.nutritional_value += 1

    def grow_and_age(self, age_for: int) -> None:
        print(f"[make {self.name} grow and age for {age_for} days]")
        for i in range(age_for):
            self.grow()
            self.age()

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.update_plant_type("Seed")
        self.number_of_seeds = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.number_of_seeds}")

    def grow(self, growth_rate: float = 8.0) -> None:
        super().grow(growth_rate)

    def bloom(self, number_of_seeds: int = 0) -> None:
        super().bloom()
        self.number_of_seeds += number_of_seeds


def show_plant_statistics(plant_obj: Plant) -> None:
    print(f"[statistics for {plant_obj.name.capitalize()}]")
    plant_obj.show_statistics()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    days_to_check = [30, 400]
    for days in days_to_check:
        print(
            f"Is {days} days more than a year?"
            f" -> {Plant.older_than_a_year(days)}"
        )

    print("\n", end="")
    flower = Flower("rose", 15.0, 10, "red")
    flower.creation_log()
    show_plant_statistics(flower)
    print(f"[asking the {flower.name} to grow and bloom]")
    flower.grow()
    flower.bloom()
    flower.show()
    show_plant_statistics(flower)

    print("\n", end="")
    tree = Tree("oak", 200.0, 365, 5.0)
    tree.creation_log()
    show_plant_statistics(tree)
    print(f"[asking the {tree.name} to produce shade]")
    tree.produce_shade()
    show_plant_statistics(tree)

    print("\n", end="")
    seed = Seed("sunflower", 80.0, 45, "yellow")
    seed.creation_log()
    print(f"[make {seed.name} grow, age and bloom]")
    seed.bloom(42)
    seed.grow(30)
    seed.age(20)
    seed.show()
    show_plant_statistics(seed)

    print("\n", end="")
    unknown = Plant.create_anonymous()
    unknown.creation_log()
    show_plant_statistics(unknown)

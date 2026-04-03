class Plant:
    def __init__(self, name: str, height: float = 0.0,
                 age_of_plant: int = 0) -> None:
        self.name = name
        self._height = height if height >= 0 else 0.0
        self._age_of_plant = age_of_plant if age_of_plant >= 0 else 0

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age_of_plant} days old")

    def grow(self, growth_rate: float = 0.8) -> None:
        self._height = round(self._height + growth_rate, 2)

    def age(self) -> None:
        self._age_of_plant += 1

    def creation_log(self) -> None:
        print("Plant created: ", end="")
        self.show()

    def set_height(self, height_passed) -> None:
        if (height_passed < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height_passed
            print(f"Height updated: {round(self._height)}cm")

    def set_age(self, age_passed) -> None:
        if (age_passed < 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
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


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)
    plant.creation_log()

    print("\n", end="")

    plant.set_height(25.0)
    plant.set_age(30)

    print("\n", end="")

    plant.set_height(-5)
    plant.set_age(-11)

    plant.current_state()

class GardenError(Exception):
    def __init__(self, message="A garden error occurred") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error") -> None:
        super().__init__(message)


class Plant():
    def __init__(self, name: str = "Unknown",
                 water_level: int = 5, water_available: int = 0) -> None:
        self.name = name
        self.water_level = water_level
        self.water_available = water_available

    def grow_plant(self) -> None:
        if self.water_level < 3:
            raise PlantError(f"The {self.name} plant is wilting!")
        else:
            print(f"The {self.name} plant is growing!")

    def water_plant(self) -> None:
        if self.water_available == 0:
            raise WaterError("Not enough water in the tank!")
        else:
            self.water_available -= 1
            print(f"The {self.name} plant has been watered!")


def test_custom_errors() -> None:
    plant_err = Plant("tomato", 1, 0)

    print("\nTesting PlantError...")
    try:
        plant_err.grow_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        plant_err.water_plant()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        plant_err.grow_plant()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        plant_err.water_plant()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_custom_errors()

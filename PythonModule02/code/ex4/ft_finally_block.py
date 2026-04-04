class GardenError(Exception):
    def __init__(self, message="A garden error occurred"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


class Plant():
    def __init__(self, name: str = "Unknown"):
        self.name = name

    def water_plant(self) -> None:
        if self.name == self.name.capitalize():
            print(f"Watering {self.name}: [OK]")
        else:
            raise PlantError(f"Invalid plant name to water: '{self.name}'")


def test_watering_system(state_of_data: str, plants: list[Plant]) -> None:
    print(f"\nTesting {state_of_data} plants...")
    print("Opening watering system")
    try:
        for plant in plants:
            plant.water_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


def run_test_watering_system() -> None:
    valid_plants = [
        Plant("Tomato"),
        Plant("Lettuce"),
        Plant("Carrots"),
    ]

    invalid_plants = [
        Plant("Tomato"),
        Plant("lettuce"),
        Plant("Carrots"),
    ]

    test_watering_system("valid", valid_plants)
    test_watering_system("invalid", invalid_plants)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    run_test_watering_system()

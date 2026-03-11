class SecurePlant:
    def __init__(self, name: str, height: int, age_of_plant: int) -> None:
        self.name = name
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age_of_plant)

    def set_height(self, height_passed) -> None:
        if (height_passed < 0):
            print(
                f"""\nInvalid operation attempted: """
                f"""height {height_passed}cm [REJECTED]"""
            )
            print("Security: Negative height rejected")
        else:
            self.height = height_passed
            print(f"Height updated: {self.height}cm [OK]")

    def set_age(self, age_passed) -> None:
        if (age_passed < 0):
            print(
                f"\nInvalid operation attempted: """
                f"""age {age_passed}days [REJECTED]"""
            )
            print("Security: Impossible age value rejected")
        else:
            self.age_of_plant = age_passed
            print(f"Age updated: {self.age_of_plant} days [OK]")

    def get_height(self) -> int:
        return (self.height)

    def get_age(self) -> int:
        return (self.age_of_plant)

    def current_plant(self):
        print(
            f"""\nCurrent plant: {self.name} """
            f"""({self.height}cm, {self.age_of_plant} days)"""
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(-5)
    plant.current_plant()

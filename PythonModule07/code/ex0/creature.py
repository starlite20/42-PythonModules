from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract base class representing a Creature card."""

    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        """Abstract method to perform an attack."""
        pass

    def describe(self) -> str:
        """Concrete method returning a standard description."""
        return f"{self.name} is a {self.creature_type} type creature."


class Flameling(Creature):
    """Concrete Fire type base creature."""

    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    """Concrete Fire type evolved creature."""

    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire")

    def attack(self) -> str:
        return "Pyrodon uses Inferno!"


class Aquabub(Creature):
    """Concrete Water type base creature."""

    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return "Aquabub uses Splash!"


class Torragon(Creature):
    """Concrete Water type evolved creature."""

    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return "Torragon uses Tidal Wave!"

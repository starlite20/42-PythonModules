from abc import ABC, abstractmethod

from ex0.creature import (Aquabub, Creature, Flameling, Pyrodon, Torragon)


class CreatureFactory(ABC):
    """Abstract factory for creating Creature objects."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create a base level creature."""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create an evolved level creature."""
        pass


class FlameFactory(CreatureFactory):
    """Concrete factory for the Fire creature family."""

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Concrete factory for the Water creature family."""

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()

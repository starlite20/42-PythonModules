from abc import ABC, abstractmethod

from ex1.creature import (
    Bloomelle,
    Creature,
    Morphagon,
    Shiftling,
    Sproutling,
)


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


class HealingCreatureFactory(CreatureFactory):
    """Concrete factory for the Healing creature family."""

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    """Concrete factory for the Transform creature family."""

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
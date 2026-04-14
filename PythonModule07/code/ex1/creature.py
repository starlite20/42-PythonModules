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


class HealCapability(ABC):
    """Abstract capability for healing."""

    @abstractmethod
    def heal(self) -> str:
        """Abstract method to heal."""
        pass


class TransformCapability(ABC):
    """Abstract capability for transforming state."""

    def __init__(self) -> None:
        self._is_transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """Abstract method to transform."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Abstract method to revert."""
        pass


class Sproutling(Creature, HealCapability):
    """Concrete Grass type base creature with healing."""

    def __init__(self) -> None:
        Creature.__init__(self, "Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling uses Absorb to heal!"


class Bloomelle(Creature, HealCapability):
    """Concrete Grass type evolved creature with healing."""

    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass")

    def attack(self) -> str:
        return "Bloomelle uses Solar Beam!"

    def heal(self) -> str:
        return "Bloomelle uses Floral Healing!"


class Shiftling(Creature, TransformCapability):
    """Concrete Normal type base creature with transform."""

    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._is_transformed:
            return "Shiftling uses Shadow Sneak!"
        return "Shiftling uses Tackle!"

    def transform(self) -> str:
        self._is_transformed = True
        return "Shiftling transforms into a shadowy form!"

    def revert(self) -> str:
        self._is_transformed = False
        return "Shiftling reverts to its normal form!"


class Morphagon(Creature, TransformCapability):
    """Concrete Normal type evolved creature with transform."""

    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._is_transformed:
            return "Morphagon uses Phantom Force!"
        return "Morphagon uses Slash!"

    def transform(self) -> str:
        self._is_transformed = True
        return "Morphagon transforms into a phantom form!"

    def revert(self) -> str:
        self._is_transformed = False
        return "Morphagon reverts to its normal form!"

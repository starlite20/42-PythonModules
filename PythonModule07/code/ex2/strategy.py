from abc import ABC, abstractmethod
from typing import Any


class BattleStrategy(ABC):
    """Abstract class defining a battle strategy."""

    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        """Check if the strategy is valid for the creature."""
        pass

    @abstractmethod
    def act(self, creature: Any) -> list[str]:
        """Execute the strategy actions and return log strings."""
        pass


class NormalStrategy(BattleStrategy):
    """Strategy for basic creatures."""

    def is_valid(self, creature: Any) -> bool:
        """Suitable for any creature."""
        return True

    def act(self, creature: Any) -> list[str]:
        try:
            return [creature.attack()]
        except Exception:
            return []


class AggressiveStrategy(BattleStrategy):
    """Strategy for transforming creatures."""

    def is_valid(self, creature: Any) -> bool:
        """Check for transform capabilities."""
        return (hasattr(creature, "transform") and
                hasattr(creature, "revert") and
                hasattr(creature, "attack"))

    def act(self, creature: Any) -> list[str]:
        try:
            return [
                creature.transform(),
                creature.attack(),
                creature.revert()
            ]
        except Exception:
            return []


class DefensiveStrategy(BattleStrategy):
    """Strategy for healing creatures."""

    def is_valid(self, creature: Any) -> bool:
        """Check for healing capabilities."""
        return (hasattr(creature, "attack") and
                hasattr(creature, "heal"))

    def act(self, creature: Any) -> list[str]:
        try:
            return [
                creature.attack(),
                creature.heal()
            ]
        except Exception:
            return []
from abc import ABC, abstractmethod
from typing import cast

from ex0.creature import Creature
from ex1.creature import HealCapability, TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}'"
                f" for this aggressive strategy"
            )
        c_transform = cast(TransformCapability, creature)
        return [
            c_transform.transform(),
            creature.attack(),
            c_transform.revert()
        ]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}'"
                f" for this defensive strategy"
            )
        c_heal = cast(HealCapability, creature)
        return [
            creature.attack(),
            c_heal.heal()
        ]

from typing import Any

from ex0 import AquaFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    NormalStrategy,
)


def battle(opponents: list[tuple[Any, BattleStrategy]]) -> None:
    """Simulate a tournament between all opponents."""
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strat1 = opponents[i]
            factory2, strat2 = opponents[j]

            try:
                c1 = factory1.create_base()
                c2 = factory2.create_base()
            except Exception as e:
                print(f"Factory error: {e}")
                continue

            print(f"--- Fight: {c1.name} vs {c2.name} ---")

            if not strat1.is_valid(c1):
                print(f"Invalid strategy for {c1.name}!")
            else:
                for action in strat1.act(c1):
                    print(action)

            if not strat2.is_valid(c2):
                print(f"Invalid strategy for {c2.name}!")
            else:
                for action in strat2.act(c2):
                    print(action)

            print()


def main() -> None:
    """Main execution function setting up the tournament."""
    opponents: list[tuple[Any, BattleStrategy]] = [
        (FlameFactory(), NormalStrategy()),
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
        # Invalid tuple to test error handling:
        (FlameFactory(), DefensiveStrategy()),
    ]

    battle(opponents)


if __name__ == "__main__":
    main()

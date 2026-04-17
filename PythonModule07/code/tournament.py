from typing import Any

from ex0 import AquaFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    NormalStrategy,
)
from ex0.creature import Creature


def run_tournament(
    name: str,
    desc: str,
    opponents: list[tuple[Any, BattleStrategy]]
) -> None:
    print(f"Tournament {name}")
    print(f"[ {desc} ]")
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strat1 = opponents[i]
            factory2, strat2 = opponents[j]

            c1: Creature = factory1.create_base()
            c2: Creature = factory2.create_base()

            print("\n* Battle *")
            print(f"{c1.describe()}")
            print(" vs.")
            print(f"{c2.describe()}")
            print(" now fight!")

            try:
                for action in strat1.act(c1):
                    print(action)
                for action in strat2.act(c2):
                    print(action)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    run_tournament(
        "0 (basic)",
        "(Flameling+Normal), (Healing+Defensive)",
        [
            (FlameFactory(), NormalStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy()),
        ]
    )

    print()

    run_tournament(
        "1 (error)",
        "(Flameling+Aggressive), (Healing+Defensive)",
        [
            (FlameFactory(), AggressiveStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy()),
        ]
    )

    print()

    run_tournament(
        "2 (multiple)",
        "(Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)",
        [
            (AquaFactory(), NormalStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy()),
            (TransformCreatureFactory(), AggressiveStrategy()),
        ]
    )


if __name__ == "__main__":
    main()

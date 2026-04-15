from ex0.factory import CreatureFactory
from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)


def test_healing_factory(factory: CreatureFactory) -> None:
    try:
        base = factory.create_base()
        evolved = factory.create_evolved()

        print("base:")
        print(base.describe())
        print(base.attack())
        print(base.heal())

        print("evolved:")
        print(evolved.describe())
        print(evolved.attack())
        print(evolved.heal())

    except Exception as e:
        print(f"An error occurred: {e}")


def test_transform_factory(factory: CreatureFactory) -> None:
    try:
        base = factory.create_base()
        evolved = factory.create_evolved()

        print("base:")
        print(base.describe())
        print(base.attack())
        print(base.transform())
        print(base.attack())
        print(base.revert())

        print("evolved:")
        print(evolved.describe())
        print(evolved.attack())
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())

    except Exception as e:
        print(f"An error occurred: {e}")


def main() -> None:
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    print("Testing Creature with healing capability")
    test_healing_factory(heal_factory)

    print("\nTesting Creature with transform capability")
    test_transform_factory(transform_factory)


if __name__ == "__main__":
    main()

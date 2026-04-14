from ex1 import (
    HealCapability,
    HealingCreatureFactory,
    TransformCapability,
    TransformCreatureFactory,
)
from ex1.factory import CreatureFactory


def test_healing_factory(factory: CreatureFactory) -> None:
    """Test description, attack, and heal for healing creatures."""
    try:
        base = factory.create_base()
        evolved = factory.create_evolved()

        print(base.describe())
        print(base.attack())
        if isinstance(base, HealCapability):
            print(base.heal())

        print(evolved.describe())
        print(evolved.attack())
        if isinstance(evolved, HealCapability):
            print(evolved.heal())

    except Exception as e:
        print(f"An error occurred: {e}")


def test_transform_factory(factory: CreatureFactory) -> None:
    """Test description, attack, transform, attack, and revert."""
    try:
        base = factory.create_base()
        evolved = factory.create_evolved()

        print(base.describe())
        print(base.attack())
        if isinstance(base, TransformCapability):
            print(base.transform())
            print(base.attack())
            print(base.revert())

        print(evolved.describe())
        print(evolved.attack())
        if isinstance(evolved, TransformCapability):
            print(evolved.transform())
            print(evolved.attack())
            print(evolved.revert())

    except Exception as e:
        print(f"An error occurred: {e}")


def main() -> None:
    """Main execution function."""
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    print("--- Testing Healing Factory ---")
    test_healing_factory(heal_factory)

    print("\n--- Testing Transform Factory ---")
    test_transform_factory(transform_factory)


if __name__ == "__main__":
    main()

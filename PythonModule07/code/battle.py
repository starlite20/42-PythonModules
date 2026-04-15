from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    try:
        base_creature = factory.create_base()
        evolved_creature = factory.create_evolved()

        print(base_creature.describe())
        print(base_creature.attack())

        print(evolved_creature.describe())
        print(evolved_creature.attack())

    except Exception as e:
        print(f"An error occurred while testing factory: {e}")


def make_them_fight(
    factory1: CreatureFactory,
    factory2: CreatureFactory
) -> None:
    try:
        creature1 = factory1.create_base()
        creature2 = factory2.create_base()

        print(creature1.describe())
        print("vs.")
        print(creature2.describe())
        print("fight!")
        print(creature1.attack())
        print(creature2.attack())

    except Exception as e:
        print(f"An error occurred during the fight: {e}")


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    print("Testing factory")
    test_factory(flame_factory)

    print("\nTesting factory")
    test_factory(aqua_factory)

    print("\nTesting battle")
    make_them_fight(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()

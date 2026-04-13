import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print("Testing record light spell: ", end="")
    print(alchemy.grimoire.light_spellbook.light_spell_record(
        "Fantasy", "Earth, wind and fire"))


if __name__ == "__main__":
    main()

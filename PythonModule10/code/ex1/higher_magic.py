from collections.abc import Callable


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(
    spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} with {power} power"

    def heal(target: str, power: int) -> str:
        return f"Heals {target} for {power} HP"

    def is_strong(target: str, power: int) -> bool:
        return power >= 10

    print("Testing spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    if callable(combined_spell):
        result = combined_spell("Dragon", 10)
        print(f"Combined spell result: {result[0]}, {result[1]}")
    print()

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    if callable(mega_fireball):
        original = fireball("Goblin", 10)
        amplified = mega_fireball("Goblin", 10)
        print(f"Original: {original}, Amplified: {amplified}")
    print()

    print("Testing conditional caster...")
    safe_cast = conditional_caster(is_strong, fireball)
    if callable(safe_cast):
        print(safe_cast("Orc", 15))
        print(safe_cast("Orc", 5))
    print()

    print("Testing spell sequence...")
    combo = spell_sequence([fireball, heal, fireball])
    if callable(combo):
        results = combo("Demon", 20)
        for res in results:
            print(res)

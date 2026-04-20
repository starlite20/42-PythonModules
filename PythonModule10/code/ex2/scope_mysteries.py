from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def inner() -> int:
        nonlocal count
        count += 1
        return count

    return inner


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total = initial_power

    def inner(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return inner


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def inner(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return inner


def memory_vault() -> dict[str, Callable]:
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        if key in vault:
            return vault[key]
        return "Memory not found"

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print()

    print("Testing spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")
    print()

    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))
    print()

    print("Testing memory vault...")
    my_vault = memory_vault()
    my_vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {my_vault['recall']('secret')}")
    print(f"Recall 'unknown': {my_vault['recall']('unknown')}")

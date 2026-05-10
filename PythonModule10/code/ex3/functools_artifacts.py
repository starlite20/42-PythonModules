import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    op_func: Callable[[int, int], int]
    if operation == "add":
        op_func = operator.add
    elif operation == "multiply":
        op_func = operator.mul
    elif operation == "max":
        op_func = max
    elif operation == "min":
        op_func = min
    else:
        return 0

    return functools.reduce(op_func, spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[..., str]]:
    fire_spell = functools.partial(base_enchantment, power=50, element="Fire")
    ice_spell = functools.partial(base_enchantment, power=50, element="Ice")
    lightning_spell = functools.partial(
        base_enchantment, power=50, element="Lightning"
    )

    return {
        "fire": fire_spell,
        "ice": ice_spell,
        "lightning": lightning_spell
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@functools.singledispatch
def _dispatch_logic(arg: Any) -> str:
    return "Unknown spell type"


@_dispatch_logic.register
def _(arg: int) -> str:
    return f"Damage spell: {arg} damage"


@_dispatch_logic.register
def _(arg: str) -> str:
    return f"Enchantment: {arg}"


@_dispatch_logic.register
def _(arg: list) -> str:
    return f"Multi-cast: {len(arg)} spells"


def spell_dispatcher() -> Callable[[Any], str]:
    """Return the singledispatch system."""
    return _dispatch_logic


if __name__ == "__main__":
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")
    print()

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")
    print()

    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["spell1", "spell2", "spell3"]))
    print(dispatcher(3.14))

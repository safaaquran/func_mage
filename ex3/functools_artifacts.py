from functools import partial, reduce, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if spells == []:
        return 0
    else:
        if operation == "add":
            combined_spell: int = reduce(add, spells)
        elif operation == "max":
            combined_spell: int = max(spells)
        elif operation == "min":
            combined_spell: int = min(spells)
        elif operation == "mul":
            combined_spell: int = reduce(mul, spells)
        else:
            raise ValueError("Unknown operation")
    return combined_spell


def spell(power: int, element: str, target: str) -> str:
    return f"{element} hits {target} with power {power}"


def partial_enchanter(
        base_enchantment: Callable
        ) -> dict[str, Callable]:
    version_1 = partial(base_enchantment, 50, element="fire")
    version_2 = partial(base_enchantment, 50, element="heal")
    version_3 = partial(base_enchantment, 50, element="ice")
    return {
        "fire": version_1,
        "heal": version_2,
        "ice": version_3
        }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        return 0
    if n < 2:
        return n
    else:
        return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(s):
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(s: int):
        return f"Damage spell: {s} damage"

    @dispatcher.register(str)
    def _(s: str):
        return f"Enchantment: {s}"

    @dispatcher.register(list)
    def _(s: list[Any]):
        return "Multi-cast: 3 spells"
    return dispatcher


print("Testing spell reducer...")
combined_spell: list[int] = [50, 40, 10]
print("Sum:", spell_reducer(combined_spell, "add"))
print("Product:", spell_reducer(combined_spell, "mul"))
print("Max:", spell_reducer(combined_spell, "max"))
print("Min:", spell_reducer(combined_spell, "min"))
# print("MaX:", spell_reducer(combined_spell, "maX"))

print("\ntesting partial enchanter...")
pe = partial_enchanter(spell)
print(pe["fire"](target="wizard"))
print(pe["heal"](target="dragon"))
print(pe["ice"](target="baby dragon"))

print("\nTesting memoized fibonacci...")
print("Fib(0):", memoized_fibonacci(0))
print("Fib(1):", memoized_fibonacci(-1))
print("Fib(10):", memoized_fibonacci(10))
print("Fib(15):", memoized_fibonacci(15))
# print(memoized_fibonacci.cache_info())

print("\nTesting spell dispatcher...")

# Ancient Library Test Data
spell_powers = [15, 14, 24, 39, 11, 30]
fibonacci_tests = [20, 15, 15]

print("\nTesting spell dispatcher...")

sp = spell_dispatcher()
print(sp(5))
# spell_dispatcher("fireball")

import functools
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if spells == []:
        return 0
    else:
        if operation == "add":
            combined_spell: int = functools.reduce(add, spells)
        elif operation == "max":
            combined_spell: int = max(spells)
        elif operation == "min":
            combined_spell: int = min(spells)
        elif operation == "mul":
            combined_spell: int = functools.reduce(mul, spells)
    return combined_spell


def spell(power: int, element: str, target: str) -> str:
    return f" {element} hits {target} with power{power}"


def partial_enchanter(base_enchantment:	Callable)
-> dict[str, Callable]:
    version_1 =
    

print("Testing spell reducer...")
combined_spell: list[int] = [50, 40, 10]
print("Sum:", spell_reducer(combined_spell, "add"))
print("Product:", spell_reducer(combined_spell, "mul"))
print("Max:", spell_reducer(combined_spell, "max"))
print("Min:", spell_reducer(combined_spell, "min"))
# print("Max:", spell_reducer(combined_spell, "maX"))
# Ancient Library Test Data
spell_powers = [15, 14, 24, 39, 11, 30]
operations = ['add', 'multiply', 'max', 'min']
fibonacci_tests = [20, 15, 15]

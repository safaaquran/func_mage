from collections.abc import Callable


def mage_counter() -> Callable:
    counter: int = 0

    def counter_func() -> int:
        nonlocal counter
        counter += 1
        return counter
    return counter_func


def spell_accumulator(initial_power: int) -> Callable:

    def adder(addition: int) -> int:
        total_power = initial_power + addition
        return total_power
    return adder


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name: str) -> str:
        enchantedDescription: str = enchantment_type+" "+item_name
        return enchantedDescription
    return enchantment


def memory_vault() -> dict[str, Callable]:
    dictionary: dict = {}

    def store(key: str, value: int) -> str:
        nonlocal dictionary
        dictionary[key] = value
        return f"Store '{key}' = {value}"

    def recall(key: str) -> str:
        nonlocal dictionary
        if key in dictionary:
            return f"Recall '{key}': {dictionary[key]}"
        else:
            return ("Recall ’unknown’: Memory not found")
    return {"Store": store, "Recall": recall}


enchantment_types = ['Earthen', 'Flaming', 'Radiant']
items_to_enchant = ['Amulet', 'Ring', 'Shield', 'Sword']

mc = mage_counter()
print("counter_a call 1: ", end="")
print(mc())
print("counter_a call 2: ", end="")
print(mc())
mc2 = mage_counter()
print("counter_b call 1: ", end="")
print(mc2())

base: int = 100
addition: int = 20
print("\nTesting spell accumulator... ")
sa = spell_accumulator(base)
print(f"Base {base}, add {addition}: {sa(20)}")
print(f"Base {base}, add {addition}: {sa(30)}")

print("\nTesting enchantment factory... ")
ef = enchantment_factory(enchantment_types[1])
print(ef(items_to_enchant[3]))
ef = enchantment_factory(enchantment_types[2])
print(ef(items_to_enchant[1]))

print("\nTesting memory vault... ")
mv = memory_vault()
print(mv["Store"]("secret", 42))
print(mv["Recall"]("secret"))
print(mv["Recall"]("safaa"))

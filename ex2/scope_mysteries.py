from typing import Callable
def mage_counter() -> Callable:
    counter: int = 0
    def counter_func() -> int:
        nonlocal counter
        counter += 1
        return counter
    return counter_func

mc = mage_counter()
print("counter_a call 1: ", end = "")
print(mc())
print("counter_a call 2:", end = "")
print(mc())
mc2 = mage_counter()
print("counter_b call 1: ",end = "")
print(mc2())

initial_powers = [55, 78, 26]
power_additions = [7, 19, 20, 15, 20]
enchantment_types = ['Earthen', 'Flaming', 'Radiant']
items_to_enchant = ['Amulet', 'Ring', 'Wand', 'Shield']

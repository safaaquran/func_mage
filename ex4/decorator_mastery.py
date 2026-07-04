from typing import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def decorator() -> str:
        print("casting", func.__name__, end="...\n")
        start = time.time()
        f = func()
        time.sleep(0.002)
        end = time.time()
        executed = end - start
        print(f"Spell completed in {executed:.3f} seconds")
        return f
    return decorator


@spell_timer
def spell() -> str:
    return "fireball cast"


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> str:

        def wrapper_func(power: int) -> str:
            if power >= min_power:
                return func(power)
            else:
                return "Insufficient power for this spell"
        return wrapper_func
    return decorator


@power_validator(50)
def healing_power(power: int) -> str:
    return f"power: {power} accepted to heal!"


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> str:

        def wrapper(name: str) -> str:
            num: int = 1
            for i in range(1, max_attempts+1):
                if num <= max_attempts:
                    raise Exception("Spell failed, retrying... (attempt {i}/{max_attempts})")
                num += 1
                if i == max_attempts +1 :
                        print(f"Spell casting failed after {max_attempts} attempts ")
                else:
                    return func(name)
        return wrapper
    return decorator
        

@retry_spell(3)
def spell_casting(spell_name: str) -> str:
    return f"{spell_name} spelled !"


print("Testing spell timer...")
f = spell()
print(f"Result: {f}!")
print()

print("testing power validator...")
print(healing_power(40))
print()

print("testing retry spell...")
print(spell_casting("Wgh"))
# Master's Tower Test Data
test_powers = [16, 6, 21, 16]
spell_names = ['earthquake', 'heal', 'darkness', 'flash']
mage_names = ['River', 'Rowan', 'Sage', 'Riley', 'Morgan', 'Zara']
invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

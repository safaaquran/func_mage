from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def decorator() -> str:
        print("casting", func.__name__, end="...\n")
        start = time.time()
        f = func()
        end = time.time()
        executed = end - start
        print(f"Spell completed in {executed:.3f} seconds")
        return f
    return decorator


@spell_timer
def spell() -> str:
    time.sleep(0.002)
    return "fireball cast"


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> str:

        @wraps(func)
        def wrapper_func(*args, **kwargs) -> str:
            power = None
            for arg in args:
                if isinstance(arg, int) and not isinstance(arg, bool):
                    power = arg
            if power is None:
                power = kwargs["power"]
            if power >= min_power:
                return func(*args, **kwargs)
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
            for i in range(1, max_attempts+1):
                try:
                    return func(name)
                except Exception:
                    print(
                        f"Spell failed, retrying... attempt:"
                        f"{i}/{max_attempts}"
                        )
            print(f"Spell casting failed after {max_attempts} attempts")
        return wrapper
    return decorator


@retry_spell(3)
def spell_casting(spell_name: str) -> str:

    return f"{spell_name} spelled !"


@retry_spell(3)
def spell_casting_invalid(name: str) -> str:
    raise ValueError("invalid")


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        else:
            for c in name:
                if not c.isalpha() and not c.isspace():
                    return False
            return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


print("Testing spell timer...")
f2 = spell()
# print("-----", spell.__name__)
print(f"Result: {f2}!")
print()

print("testing power validator...")
print(healing_power(40))
print()

print("testing retry spell...")

spell_casting_invalid("wajddd")
print(spell_casting("Waaaaaaaaaaagh"))
print()

print("Testing MageGuild...")
print(MageGuild.validate_mage_name("hi"))
print(MageGuild.validate_mage_name("saf aaa"))
guild = MageGuild()
print(guild.cast_spell("safaa", 19))
print(guild.cast_spell("w", 4))

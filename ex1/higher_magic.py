from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"fireball hits {target}"


def heal(target: str, power: int) -> str:
    return f"Heals {target}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (
            spell1(target, power),
            spell2(target, power)
            )
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifier

#def conditional_caster(condition: Callable, spell: Callable) -> Callable:


#def spell_sequence(spells:	list[Callable]) -> Callable:


if __name__ == "__main__":
    test_values = [23, 8, 21]
    test_target = "Dragon"
    combined_spell = spell_combiner(fireball, heal)
    result: tuple[str, str] = combined_spell(test_target, 23)
    print("Testing spell combiner...")
    print("Combined spell result: ", end="")
    print(result[0], end=", ")
    print(result[1])
    print("Testing power amplifier... ")
    mega_fireball = power_amplifier(fireball, 3)
    mf = mega_fireball(test_target, 10)
    print(f"Original: ")

from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"fireball hits {target}, with {power} power"


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


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def string_returner() -> str:
        return "Spell fizzled"

    def new_spell(target: str, power: int) -> str:
        if condition("dragon", 0):
            return spell(target, power)
        else:
            return string_returner()
    return new_spell


def spell_sequence(spells:	list[Callable]) -> Callable:
    def spells_list(target: str, power: int) -> list[str]:
        spellsResults: list[str] = []
        for spell in spells:
            spellsResults.append(spell(target, power))
        return spellsResults
    return spells_list


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
    power: int = 3
    mega_fireball = power_amplifier(fireball, power)
    print(f"Orginal: {power}", end=" ")
    print(f"Amplified {mega_fireball(test_target, 10)}")

    def condition(target: str, power: int) -> bool:
        return (power > 0)
    print("\ntesting conditional caster...")
    cc = conditional_caster(condition, fireball)
    print(cc(test_target, 2))
    print("\ntesting spell sequence...")
    spells: list[Callable] = [heal, fireball, heal]
    ss = spell_sequence(spells)
    print(ss(test_target, 3))

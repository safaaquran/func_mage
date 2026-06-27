def artifact_sorter(artifacts:	list[dict]) -> list[dict]:
    sortedArtifacts: list[dict] = sorted(
        artifacts, key=lambda arti: arti["power"], reverse=True
        )
    return sortedArtifacts


def power_filter(mages:	list[dict], min_power:	int) -> list[dict]:
    filtered: list[dict] = list(filter(
        lambda m: m["power"] >= min_power, mages
        ))
    return filtered


def spell_transformer(spells: list[str]) -> list[str]:
    stared: list[str] = list(map(
        lambda s: "* " + s + " *", spells
        ))
    return stared


def mage_stats(mages: list[dict]) -> dict:
    mn: int = min(mages, key=lambda m: m["power"])["power"]
    mx: int = max(mages, key=lambda m: m["power"])["power"]
    summ: float = sum(map(lambda a: a["power"], mages))
    leng: int = len(mages)
    avg: float = round(summ/leng, 2)
    return {
        "min_power": mn,
        "max_power": mx,
        "avg_power": avg
        }


if __name__ == "__main__":
    print("Testing artifact sorter...")
    artifacts = [
            {'name': 'Crystal Orb', 'power': 85, 'type': 'accessory'},
            {'name': 'Fire Staff', 'power': 92, 'type': 'armor'},
            #{'name': 'Storm Crown', 'power': 115, 'type': 'accessory'}
        ]
    mages = [
        {'name': 'Storm', 'power': 62, 'element': 'lightning'},
        {'name': 'Ember', 'power': 98, 'element': 'lightning'},
        {'name': 'River', 'power': 50, 'element': 'ice'},
        {'name': 'Rowan', 'power': 66, 'element': 'light'},
        {'name': 'Ash', 'power': 57, 'element': 'lightning'}
    ]
    spells = ['fireball', 'heal', 'shield']
    result: list[dict] = artifact_sorter(artifacts)
    for i, artifact in enumerate(result):
        print(f"{artifact['name']} ({artifact['power']}power)", end = " ")
        if i != len(artifact) - 1:
            print("comes before", end = " ")
    print("\nTesting spell transformer...")
    spell: list[str] = spell_transformer(spells)
    for stared in spell:
        print(stared, end = " ")
    print()
    print("\ntesting the graeter power...")
    greater_power :list[dict] = power_filter(mages, 65)
    for mage in greater_power:
        print(f"{mage['name']} because the power is:{mage['power']}")
    print("\ntesting mage stats...")
    stats: dict = mage_stats(mages)
    print (
    f"the min of mages is {stats['min_power']}\n"
    f"the max of mages is {stats['max_power']}\n"
    f"the average of mages is {stats['avg_power']}"
    )

#!usr/bin/venv python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda v: v["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda v: v["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda v: f"* {v} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda m: m['power'], mages))
    return {"max_power": max(powers),
            "min_power": min(powers),
            "avg_power": round(sum(powers) / len(powers), 2)}


if __name__ == "__main__":
    print("\n\033[43mTesting artifact sorter...\033[0m")

    artifacts = [
        {'name': 'crystal orb', 'power': 85, 'type': 'focus'},
        {'name': 'fire staff', 'power': 92, 'type': 'weapon'}
    ]
    spells = ["fireball", "heal", "shield"]
    mages = [
        {'name': 'merlin', 'power': 95, 'element': 'arcane'},
        {'name': 'morgana', 'power': 88, 'element': 'shadow'},
        {'name': 'apprentice', 'power': 20, 'element': 'water'}
    ]

    sorted_artifacts = artifact_sorter(artifacts)

    print(f"{sorted_artifacts[0]['name']} ("
          f"{sorted_artifacts[0]['power']} power) "
          f"comes before {sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)")

    print("\ntesting spell transformer...")

    print(" ".join(spell_transformer(spells)))

    print("\ntesting mage stats...")
    stats = mage_stats(mages)
    print(f"max: {stats['max_power']}, min: {stats['min_power']}, "
          f"avg: {stats['avg_power']}")

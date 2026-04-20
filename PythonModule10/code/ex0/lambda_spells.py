from typing import List, Dict, Any


def artifact_sorter(artifacts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
    )


def power_filter(
        mages: List[Dict[str, Any]],
        min_power: int) -> List[Dict[str, Any]]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not mages:
        return {
            "max_power": 0,
            "min_power": 0,
            "avg_power": 0.0
        }

    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    min_power = min(mages, key=lambda mage: mage["power"])["power"]

    avg_power = round(sum(mage["power"] for mage in mages) / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":
    artifacts_data = [
        {"name": "Crystal Orb", "power": 85, "type": "Magic"},
        {"name": "Fire Staff", "power": 92, "type": "Fire"}
    ]

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts_data)
    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power)"
        f" comes before {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )
    print()

    spells_data = ["fireball", "heal", "shield"]

    print("Testing spell transformer...")
    transformed_spells = spell_transformer(spells_data)
    print(" ".join(transformed_spells))

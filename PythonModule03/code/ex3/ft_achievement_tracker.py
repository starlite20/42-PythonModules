import random


def gen_player_achievements() -> set[str]:
    achievement_pool = [
        "First Steps",
        "Speed Runner",
        "Master Explorer",
        "Treasure Hunter",
        "Boss Slayer",
        "World Savior",
        "Crafting Genius",
        "Collector Supreme",
        "Untouchable",
        "Unstoppable",
        "Sharp Mind",
        "Strategist",
        "Hidden Path Finder"
    ]

    count = random.randint(5, 9)
    achievement_set = set(random.sample(achievement_pool, count))
    return achievement_set


def main() -> None:
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_achievements = set.union(alice, bob, charlie, dylan)
    print(f"All distinct achievements: {all_achievements}")

    common_achievements = set.intersection(alice, bob, charlie, dylan)
    print(f"\nCommon achievements: {common_achievements}\n")

    alice_only = alice.difference(set.union(bob, charlie, dylan))
    bob_only = bob.difference(set.union(alice, charlie, dylan))
    charlie_only = charlie.difference(set.union(alice, bob, dylan))
    dylan_only = dylan.difference(set.union(alice, bob, charlie))

    print(f"Only Alice has: {alice_only}")
    print(f"Only Bob has: {bob_only}")
    print(f"Only Charlie has: {charlie_only}")
    print(f"Only Dylan has: {dylan_only}")

    print(f"\nAlice is missing: {all_achievements.difference(alice)}")
    print(f"Bob is missing: {all_achievements.difference(bob)}")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}")


if __name__ == "__main__":
    main()

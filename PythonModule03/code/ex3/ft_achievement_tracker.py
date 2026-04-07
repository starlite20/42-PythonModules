import random

def gen_player_achievements():
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

def main():
    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }

    print("Player Alice:", players["Alice"])
    print("Player Bob:", players["Bob"])
    print("Player Charlie:", players["Charlie"])
    print("Player Dylan:", players["Dylan"])

    all_achievements = set.union(
        players["Alice"],
        players["Bob"],
        players["Charlie"],
        players["Dylan"]
    )
    print("All distinct achievements:", all_achievements)

    common_achievements = set.intersection(
        players["Alice"],
        players["Bob"],
        players["Charlie"],
        players["Dylan"]
    )
    print(f"\nCommon achievements:{common_achievements}\n")
    
    alice_only = players["Alice"].difference(
        set.union(players["Bob"], players["Charlie"], players["Dylan"])
    )
    bob_only = players["Bob"].difference(
        set.union(players["Alice"], players["Charlie"], players["Dylan"])
    )
    charlie_only = players["Charlie"].difference(
        set.union(players["Alice"], players["Bob"], players["Dylan"])
    )
    dylan_only = players["Dylan"].difference(
        set.union(players["Alice"], players["Bob"], players["Charlie"])
    )

    print("Only Alice has:", alice_only)
    print("Only Bob has:", bob_only)
    print("Only Charlie has:", charlie_only)
    print("Only Dylan has:", dylan_only)

    print("\nAlice is missing:", all_achievements.difference(players["Alice"]))
    print("Bob is missing:", all_achievements.difference(players["Bob"]))
    print("Charlie is missing:", all_achievements.difference(players["Charlie"]))
    print("Dylan is missing:", all_achievements.difference(players["Dylan"]))


if __name__ == "__main__":
    main()
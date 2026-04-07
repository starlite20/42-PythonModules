import random


def main():
    print("=== Game Data Alchemist ===")

    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")

    # all names capitalized
    capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized}")

    # only already-capitalized names
    capitalized_only = [name for name in players if name==name.capitalize()]
    print(f"New list of capitalized names only: {capitalized_only}")

    # dict with random scores
    scores = {name: random.randint(0, 1000) for name in capitalized}
    print(f"Score dict: {scores}")

    # average
    avg = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {avg}")

    # high scores dict
    high_scores = {name: score for name, score in scores.items() if score > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
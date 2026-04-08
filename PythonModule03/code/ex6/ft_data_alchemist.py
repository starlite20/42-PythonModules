import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = ['Alice', 'bob', 'Charlie', 'dylan',
               'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")

    capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized}")

    capitalized_only = [name for name in players if name == name.capitalize()]
    print(f"New list of capitalized names only: {capitalized_only}")

    scores = {name: random.randint(0, 1000) for name in capitalized}
    print(f"Score dict: {scores}")

    avg = round(sum(scores[name] for name in scores) / len(scores), 2)
    print(f"Score average is {avg}")

    high_scores = {name: scores[name]
                   for name in scores if scores[name] > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()

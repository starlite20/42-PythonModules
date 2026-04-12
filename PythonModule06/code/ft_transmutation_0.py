import alchemy.transmutation.recipes as recipes


def main() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print("Testing lead to gold: ", end="")
    print(recipes.lead_to_gold())


if __name__ == "__main__":
    main()
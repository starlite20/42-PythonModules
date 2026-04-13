import alchemy.elements as elements


def main() -> None:
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print("Testing create_earth: ", end="")
    print(elements.create_earth())


if __name__ == "__main__":
    main()

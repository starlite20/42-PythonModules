import sys
import typing


def print_file_data(file: typing.IO[str]) -> None:
    content = file.read()
    print("---\n")
    print(content)
    print("\n---")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file = None
    print("=== Cyber Archives Recovery ===")
    try:
        filename = sys.argv[1]
        print(f"Accessing file '{filename}'")
        file = open(filename, "r")
        print_file_data(file)

    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return
    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()

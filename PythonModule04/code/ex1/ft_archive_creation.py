import sys


def print_content(content: str) -> None:
    print("---\n")
    print(content, end="")
    print("\n---")


def read_print_file(filename: str) -> str | None:
    file = None
    content = None
    try:
        print(f"Accessing file '{filename}'")
        file = open(filename, "r")
        content = file.read()
        print_content(content)
    except Exception as e:
        print(f"Error opening file '{filename}': {e}\n")
        return content
    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.\n")
    return content


def add_artifact_to_content(content: str) -> str:
    archived_content = ""
    for character in content:
        if (character == "\n"):
            archived_content += "#"
        archived_content += character

    return archived_content


def write_archived_content(write_filename: str, content: str) -> None:
    writefile = None
    try:
        print(f"Saving data to '{write_filename}'")
        writefile = open(write_filename, "w")
        writefile.write(content)
        print(f"Data saved in file '{write_filename}'.")

    except Exception as e:
        print(f"Error writing to file '{write_filename}': {e}\n")

    finally:
        if writefile is not None:
            writefile.close()


def main() -> None:
    if (len(sys.argv) != 2):
        print("Usage: ft_ancient_text.py <file>\n")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    content = None
    content = read_print_file(sys.argv[1])

    if content is not None:
        archived_content = add_artifact_to_content(content)
        print("Transform data:")
        print_content(archived_content)

        write_filename = input("Enter new file name (or empty): ")
        if write_filename != "":
            write_archived_content(write_filename, archived_content)
        else:
            print("Not saving data.")


if __name__ == "__main__":
    main()

import sys


def print_content(content: str) -> None:
    print("---\n")
    print(content)
    print("\n---")


def read_artifact_print_file(filename: str) -> tuple[str, str] | None:
    file = None
    content = ""
    archived_content = ""
    try:
        print(f"Accessing file '{filename}'")
        file = open(filename, "r")
        while True:
            line = file.readline()
            if not line:
                break
            content += line
            if line[-1] == "\n":
                archived_content += line[:-1] + "#\n"
            else:
                archived_content += line + "#"
        print_content(content)
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stderr.flush()
        return None
    finally:
        if file is not None:
            file.close()
            print(f"File '{filename}' closed.")
    return (content, archived_content)


def write_archived_content(write_filename: str, content: str) -> None:
    writefile = None
    try:
        print(f"Saving data to '{write_filename}'")
        writefile = open(write_filename, "w")
        writefile.write(content)
        print(f"Data saved in file '{write_filename}'.")
    except Exception as e:
        sys.stderr.write(
            f"[STDERR] Error opening file '{write_filename}': {e}\n")
        sys.stderr.flush()
        print("Data not saved.")
    finally:
        if writefile is not None:
            writefile.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 ft_stream_management.py <filename>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    result = read_artifact_print_file(sys.argv[1])

    if result is not None:
        content, archived_content = result
        print("\nTransform data:")
        print_content(archived_content)

        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        write_filename = sys.stdin.readline()

        if write_filename != "" and write_filename[-1] == "\n":
            write_filename = write_filename[:-1]

        if write_filename != "":
            write_archived_content(write_filename, archived_content)
        else:
            print("Not saving data.")


if __name__ == "__main__":
    main()

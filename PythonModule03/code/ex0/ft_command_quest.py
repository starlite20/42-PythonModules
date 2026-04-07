import sys


def main():
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])
    arg_count = len(sys.argv) - 1

    if arg_count == 0:
        print("No arguments provided!")
    else:
        print("Arguments received:", arg_count)

        i = 1
        while i < len(sys.argv):
            print("Argument", i, ":", sys.argv[i])
            i += 1

    print("Total arguments:", len(sys.argv))


if __name__ == "__main__":
    main()

# alternative ways
# args = sys.argv[1:]

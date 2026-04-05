def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        5/0
    elif operation_number == 2:
        open("/non/existent/file", "r")
    elif operation_number == 3:
        "abc" + 5


def test_error_types() -> None:
    operations_available = [0, 1, 2, 3, 4]
    for i in operations_available:
        print(f"Testing operation {i}...")
        try:
            if (i != 4):
                garden_operations(i)
            else:
                print("Operation completed successfully")
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as e:
            print(f"Caught {e.__class__.__name__}: {e}")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()

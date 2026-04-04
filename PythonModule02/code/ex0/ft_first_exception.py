def input_temperature(input_str: str) -> int:
    print(f"\nInput data is '{input_str}'")
    return int(input_str)


def test_temperature(input_str: str) -> None:
    try:
        temp = input_temperature(input_str)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature('25')
    test_temperature('abc')
    print("\nAll tests completed - program didn't crash!")

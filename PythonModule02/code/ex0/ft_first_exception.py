def input_temperature(input_str: str) -> int:
    print(f"\nInput data is '{input_str}'")
    return int(input_str)


def call_input_temperature(input_str: str) -> None:
    try:
        temp = input_temperature(input_str)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


def test_temperature() -> None:
    call_input_temperature('25')
    call_input_temperature('abc')
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()

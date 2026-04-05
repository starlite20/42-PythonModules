def input_temperature(temp_str: str) -> int:
    print(f"\nInput data is '{temp_str}'")
    temp_val = int(temp_str)
    if (temp_val < 0):
        raise ValueError(f"{temp_val}°C is too cold for plants (min 0°C)")
    elif (temp_val > 40):
        raise ValueError(f"{temp_val}°C is too hot for plants (max 40°C)")
    else:
        return temp_val


def call_input_temperature(temp_str: str) -> None:
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


def test_temperature() -> None:
    call_input_temperature('25')
    call_input_temperature('abc')
    call_input_temperature('100')
    call_input_temperature('-50')
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()

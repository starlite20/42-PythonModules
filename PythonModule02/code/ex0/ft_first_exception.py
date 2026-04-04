def input_temperature(temp_str: string) -> int:
    try:
        temp = int(temp_str)
        return temp
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None


def test_temperature() -> None:
    temp_str = "25"
    temp = input_temperature(temp_str)
    if temp is not None:
        print(f"The temperature you entered is: {temp}°C")
    else:
        print("No valid temperature was entered.")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
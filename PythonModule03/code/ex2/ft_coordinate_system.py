import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': ")

        try:
            x_str, y_str, z_str = user_input.split(',')
        except ValueError:
            print("Invalid syntax")
            continue

        try:
            x = float(x_str.strip())
            y = float(y_str.strip())
            z = float(z_str.strip())
            return (x, y, z)
        except ValueError as e:
            for axis in (x_str, y_str, z_str):
                try:
                    float(axis.strip())
                except ValueError:
                    print(f"Error on parameter '{axis.strip()}': {e}")
                    break


def distance(point_1: tuple[float, float, float],
             point_2: tuple[float, float, float]) -> float:
    return math.sqrt(
        (point_2[0] - point_1[0]) ** 2 +
        (point_2[1] - point_1[1]) ** 2 +
        (point_2[2] - point_1[2]) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    point_1 = get_player_pos()

    print(f"Got a first tuple: {point_1}")
    print(f"It includes: X={point_1[0]}, Y={point_1[1]}, Z={point_1[2]}")

    center = (0.0, 0.0, 0.0)
    dist_center = distance(point_1, center)
    print(f"Distance to center: {round(dist_center, 4)}")

    print("Get a second set of coordinates")
    point_2 = get_player_pos()

    dist_between = distance(point_1, point_2)
    print(
        f"Distance between the 2 sets "
        f"of coordinates: {round(dist_between, 4)}"
    )


if __name__ == "__main__":
    main()

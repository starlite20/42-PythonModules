import math

def get_player_pos():
    while True:
        user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
        coordinates = user_input.split(',')

        if len(coordinates) != 3:
            print("Invalid syntax")
            continue
        
        try:
            x = float(coordinates[0].strip())
            y = float(coordinates[1].strip())
            z = float(coordinates[2].strip())
            return (x, y, z)
        except ValueError as e:
            # Find which parameter caused the error
            for axis in coordinates:
                try:
                    float(axis.strip())
                except ValueError:
                    print(f"Error on parameter '{axis.strip()}': {e}")
                    break


def distance(point_1, point_2):
    return math.sqrt(
        (point_2[0] - point_1[0]) ** 2 +
        (point_2[1] - point_1[1]) ** 2 +
        (point_2[2] - point_1[2]) ** 2
    )


def main():
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    point_1 = get_player_pos()

    print("Got a first tuple:", point_1)
    print(f"It includes: X={point_1[0]}, Y={point_1[1]}, Z={point_1[2]}")

    center = (0.0, 0.0, 0.0)
    dist_center = distance(point_1, center)
    print("Distance to center:", round(dist_center, 4))

    print("Get a second set of coordinates")
    point_2 = get_player_pos()

    dist_between = distance(point_1, point_2)
    print("Distance between the 2 sets of coordinates:", round(dist_between, 4))


if __name__ == "__main__":
    main()
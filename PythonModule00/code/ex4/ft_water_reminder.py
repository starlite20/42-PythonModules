def ft_water_reminder():
    last_watered_days = int(input("Days since last watering: "))
    if last_watered_days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
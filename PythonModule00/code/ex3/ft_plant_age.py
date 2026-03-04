def ft_plant_age():
    plant_Age = int(input("Enter plant age in days: "))
    if plant_Age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
def print_harvest_day(days_until_harvest):
    if days_until_harvest > 0:
        print_harvest_day(days_until_harvest - 1)
        print(f"Day {days_until_harvest}")


def ft_count_harvest_recursive():
    days_until_harvest = int(input("Days until harvest: "))
    print_harvest_day(days_until_harvest)
    print("Harvest time!")

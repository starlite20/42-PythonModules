def ft_count_harvest_iterative():
    days_until_harvest = int(input("Days until harvest: "))
    for days_gone in range(1, days_until_harvest + 1):
        print(f"Day {days_gone}")
    print("Harvest time!")
import sys


def main():
    print("=== Inventory System Analysis ===")

    inventory = {}
    args = sys.argv[1:]

    for param in args:
        if param.count(":") != 1:
            print(f"Error - invalid parameter '{param}'")
            continue

        parts = param.split(":")
        item_name = parts[0]
        quantity_text = parts[1]

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(quantity_text)
        except ValueError as error:
            print(f"Quantity error for '{item_name}': {error}")
            continue

        inventory[item_name] = quantity

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    for item in inventory:
        if total_quantity == 0:
            percentage = 0.0
        else:
            percentage = round((inventory[item] * 100) / total_quantity, 1)
        print(f"Item {item} represents {percentage}%")

    most_item = None
    least_item = None

    for item in inventory:
        if most_item is None or inventory[item] > inventory[most_item]:
            most_item = item
        if least_item is None or inventory[item] < inventory[least_item]:
            least_item = item

    print(f"Item most abundant: {most_item} with quantity {inventory[most_item]}")
    print(f"Item least abundant: {least_item} with quantity {inventory[least_item]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
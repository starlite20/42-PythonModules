def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    sentence = ""
    if unit == "packets":
        if (quantity > 1):
            sentence += f"{seed_type.capitalize()} seeds: "
            sentence += f"{quantity} packets available"
        else:
            sentence += f"{seed_type.capitalize()} seeds: "
            sentence += f"{quantity} packet available"
    elif unit == "grams":
        if (quantity > 1):
            sentence += f"{seed_type.capitalize()} seeds: "
            sentence += f"{quantity} grams total"
        else:
            sentence += f"{seed_type.capitalize()} seeds: "
            sentence += f"{quantity} gram total"
    elif unit == "area":
        if (quantity > 1):
            sentence += f"{seed_type.capitalize()} seeds: "
            sentence += f"covers {quantity} square meters"
        else:
            sentence += f"{seed_type.capitalize()} seeds: "
            sentence += f"covers {quantity} square meter"
    else:
        sentence += "Unknown unit type"
    print(sentence)

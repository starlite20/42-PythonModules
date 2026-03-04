def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:    
    sentence = ""
    if unit == "packets":
        if(quantity > 1):
            sentence += f"{seed_type.capitalize()} seeds: {quantity} packets available"
        else:
            sentence += f"{seed_type.capitalize()} seeds: {quantity} packet available"
    elif unit == "grams":
        if(quantity > 1):
            sentence += f"{seed_type.capitalize()} seeds: {quantity} grams total"
        else:
            sentence += f"{seed_type.capitalize()} seeds: {quantity} gram total"
    elif unit == "area":
        if(quantity > 1):
            sentence += f"{seed_type.capitalize()} seeds: covers {quantity} square meters"
        else:
            sentence += f"{seed_type.capitalize()} seeds: covers {quantity} square meter"
    else:
        sentence += "Unknown unit type"
    print(sentence)
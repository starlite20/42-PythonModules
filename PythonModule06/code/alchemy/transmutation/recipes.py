from ..elements import create_air, create_earth
from elements import create_fire, create_water
from ..potions import strength_potion


def lead_to_gold():
    return (
        f"Recipe transmuting Lead to Gold: brew "
        f"{create_air()} and {strength_potion()} mixed with {create_fire()}"
    )
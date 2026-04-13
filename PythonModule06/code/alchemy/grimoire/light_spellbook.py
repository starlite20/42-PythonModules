from .light_validator import validate_ingredients, ALLOWED_LIGHT_INGREDIENTS


def light_spell_allowed_ingredients() -> list[str]:
    return ALLOWED_LIGHT_INGREDIENTS.copy()


def light_spell_record(spell_name: str, ingredients: str) -> str:
    return (
        f"Spell recorded: {spell_name}"
        f" ({validate_ingredients(ingredients)})"
    )

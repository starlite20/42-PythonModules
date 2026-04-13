from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(ingredients: str) -> str:
    allowed_ingredients = dark_spell_allowed_ingredients()
    ingredients_list = [ingredient.strip().lower()
                        for ingredient in ingredients.split(",")]
    flag = "INVALID"
    for ingredient in ingredients_list:
        if ingredient in allowed_ingredients:
            flag = "VALID"
            break
    return f"{ingredients} - {flag}"

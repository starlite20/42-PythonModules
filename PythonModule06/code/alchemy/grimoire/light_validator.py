ALLOWED_LIGHT_INGREDIENTS = ["earth", "air", "fire", "water"]


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = ALLOWED_LIGHT_INGREDIENTS
    ingredients_list = [ingredient.strip().lower()
                        for ingredient in ingredients.split(",")]
    flag = "INVALID"
    for ingredient in ingredients_list:
        if ingredient in allowed_ingredients:
            flag = "VALID"
            break
    return f"{ingredients} - {flag}"

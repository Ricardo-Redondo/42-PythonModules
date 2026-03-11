def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    if validate_ingredients(ingredients).split("- ")[1] == "INVALID":
        return (f"Spell rejected: {spell_name} "
                f"({validate_ingredients(ingredients)})")
    return (f"Spell recorded: {spell_name} "
            f"({validate_ingredients(ingredients)})")

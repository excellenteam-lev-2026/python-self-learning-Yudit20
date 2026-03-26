def get_recipe_price(prices, optionals=[], **kwargs):
    
    if not prices:
        return 0

    total = 0

    for ingredient, prix_100g in prices.items():
        if ingredient in optionals:
            continue

        quantite = kwargs[ingredient]
        total += (prix_100g / 100) * quantite

    return total

print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))


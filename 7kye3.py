def cakes(recipe, available):
	cakes_count = min(list({ingredient_name:available.get(ingredient_name, 0) // 
						    recipe[ingredient_name] for ingredient_name in recipe}.values()))
	return cakes_count
def make_sandwich(*recipe):
    """Summarize the sandwich about to be made"""
    print("\nMaking sandwich with: ")
    for ingredients in recipe:
        print(f" - {ingredients}")

ingredient_list = []

while True:
    ingredient = input("\nEnter Ingredient (Enter 'done' to finish): ")

    if ingredient.lower() == 'done':
        break
    else:
        ingredient_list.append(ingredient)

make_sandwich(*ingredient_list) 

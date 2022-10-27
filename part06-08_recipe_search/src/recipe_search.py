
def prepare_dict(filename: str):
    recipes_list= []
    recipes = {}
    with open(filename) as file_recipes:
        for row in file_recipes:
            recipes_list.append(row.strip())
        recipes_list.append("")
    print(recipes_list)
    
    temp_list = []
    for i in recipes_list:
        temp_list.append(i)
        if i == "":     #End of recipe
            temp_list.remove("")
            recipes[temp_list[0]] = temp_list[1:]
            temp_list = []
    return recipes

def search_by_name(filename: str, word: str):
    recipes = prepare_dict(filename)
    list_found = []
    for key in recipes:
        if key.casefold().find(word.casefold()) > -1:
            list_found.append(key)
    return list_found

def search_by_time(filename: str, prep_time: int):
    recipes = prepare_dict(filename)
    list_found = []
    for key, value in recipes.items():
        if int(value[0]) <= prep_time:
            list_found.append(f"{key}, preparation time {value[0]} min")
    return list_found

def search_by_ingredient(filename: str, ingredient: str):
    recipes = prepare_dict(filename)
    list_found = []
    for key, value in recipes.items():
        for ingredients_list in value[1:]:
            if ingredients_list.casefold().find(ingredient.casefold()) > -1:
                list_found.append(f"{key}, preparation time {value[0]} min")
    return list_found


if __name__ == "__main__":
    
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)
cook_book = {}

with open('recipes.txt', 'r') as cook_book_file:
    for line in cook_book_file:
        dish = line.strip()
        cook_book [dish] = []
        ingredients_count = cook_book_file.readline()
        for i in range(int(ingredients_count)):
            ingr = cook_book_file.readline()
            ingredient_name, quantity, measure = ingr.split(' | ')
            ingredients = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure.strip()}
            cook_book[dish].append(ingredients)
        cook_book_file.readline()
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    a = []
    for dish, ingr_list in cook_book.items():
        if dish in dishes:
            for ingr in ingr_list:
                if ingr['ingredient_name'] not in a:
                    res = {'measure': ingr['measure'], 'quantity': int(ingr['quantity']) * person_count}
                    ingredients[ingr['ingredient_name']] = res
                    a.append(ingr['ingredient_name'])
                else:
                    b=int(ingr['quantity'])
                    res = {'measure': ingr['measure'], 'quantity': (int(ingr['quantity'])+b) * person_count}
                    ingredients[ingr['ingredient_name']] = res
                    a.append(ingr['ingredient_name'])
    return ingredients


print(f"\n{get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)}")



























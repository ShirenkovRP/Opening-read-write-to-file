# Нужно написать функцию, которая на вход принимает список блюд из cook_book
# и количество персон для кого мы будем готовить
# get_shop_list_by_dishes(dishes, person_count)
# На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда.


def open_file_dict(arg):  # Чтение файла и создание списка "recipes.txt"
    cook_book_def = {}
    ingredients = {}
    list_2 = []
    with open(arg, "r", encoding='utf-8') as open_file:        
        for line in open_file:
            line = line.rstrip("\n")
            if line != "":
                if line.isdigit():
                    line = int(line)
                    for file_str in range(line):
                        file_str = open_file.readline()
                        file_str = file_str.rstrip("\n")
                        ingred_list = file_str.split("|")
                        for ingred in ingred_list:
                            if ingred.strip(" ").isdigit():                            
                                ingredients["quantity"] = float(ingred.strip(" "))
                                ingredients["measure"] = ingred_list.pop(-1)
                            else:
                                ingredients["ingredient_name"] = ingred.strip(" ")
                        list_2.append(ingredients)
                        ingredients = {}                    
                    cook_book_def[name_key] = list_2
                    list_2 = []
                else:
                    name_key = line           
    return cook_book_def


def get_shop_list_by_dishes(dishes, person_count):
    order = {}
    for dish in dishes:
        if dish in cook_book:            
            for i in cook_book[dish]:
                if i["ingredient_name"] not in order:
                    order[i["ingredient_name"]] = {"measure": i["measure"], "quantity": i["quantity"]*person_count}
                else:
                    for key, value in order.items():
                        if key == i["ingredient_name"]:
                            value["quantity"] += i["quantity"]*person_count                
    return order


cook_book = open_file_dict("recipes.txt")
# print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', "Фахитос"], 2) )
for i in get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', "Фахитос"], 2):
    print(i, "\n\t", get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', "Фахитос"], 2)[i])

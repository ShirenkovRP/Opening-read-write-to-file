# Необходимо написать программу для кулинарной книги.
# Список рецептов должен храниться в отдельном файле в следующем формате:
# В одном файле может быть произвольное количество блюд.
# Читать список рецептов из этого файла.
# Соблюдайте кодстайл, разбивайте новую логику на функции и не используйте глобальных переменных.


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
                    for i in range(line):
                        i = open_file.readline()
                        i = i.rstrip("\n")
                        ingred_list = i.split("|")
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


cook_book = open_file_dict("recipes.txt")
print(cook_book)

# Необходимо объединить их в один по следующим правилам:
# Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них
# (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
# Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем

def open_file_dict(arg):  # Чтение файла
    my_list = []
    with open(arg, "r", encoding='utf-8') as open_file:
        for line in open_file:
            line = line.rstrip("\n")
            my_list.append(line)
    my_tuple = (arg, my_list, len(my_list))
    return my_tuple


def file_writen(arg, arg_2):  # Запись данных в файл
    with open(arg, "w", encoding='utf-8') as open_file:
        for i in arg_2:
            new_str1 = i[0]
            open_file.write(new_str1 + "\n")
            new_str2 = str(i[2])
            open_file.write(new_str2 + "\n")
            for k in i[1]:
                open_file.write(k + "\n")

                
file_name_1 = "1.txt"           
file_name_2 = "2.txt"      
file_name_3 = "3.txt"

new_list_1 = open_file_dict(file_name_1)
new_list_2 = open_file_dict(file_name_2)
new_list_3 = open_file_dict(file_name_3)

file_list = [new_list_1, new_list_2, new_list_3]

file_list.sort(key=lambda i: i[2])

file_writen("4.txt", file_list)

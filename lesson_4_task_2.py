print('Задача 2.')

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print('Список', my_list)

# Цикл обрабатывает список и выбирает элементы, значения которых больше значений предыдущих
new_list = [n for ind, n in enumerate(my_list) if my_list[ind] > my_list[ind - 1]]
print(f'Новый список', new_list)
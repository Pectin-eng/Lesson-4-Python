t = int(input('Введите количество отработанных сотрудником часов'))
s = int(input('Введите почасовую ставку'))
b = int(input('Введите размер премии'))

def my_func(t, s, b):
    return (t * s) + b

print(my_func(t, s, b))
from typing import Any, Union
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print('Список', my_list)
new_list = [n for ind, n in enumerate(my_list) if my_list[ind] >= my_list[ind - 1]]
print(f'Новый список', new_list)

a = 20
b = 240
list = [a, b]
print('Числа', list)
multiple20 = {el: el + 20 for el in range (20, 240) if el % 20 == 0}
print('Числа, кратные 20', multiple20)
multiple21 = {el: el + 21 for el in range (20, 240) if el % 21 == 0}
print('Числа, кратные 21', multiple21)


original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
c = counter(original_list)

print(c)

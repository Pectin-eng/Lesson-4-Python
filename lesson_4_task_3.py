print('Задача 3.')

a = 20
b = 240
list = [a, b]
print('Диапазон', list)
print('Числа, кратные 20 в заданном диапазоне', [el for el in range(a, b) if el % 20 == 0])
print('Числа, кратные 21 в заданном диапазоне', [el for el in range(a, b) if el % 21 == 0])
print('Задача 6.')

from itertools import count
from itertools import cycle

print('Первый цикл')
a = int(input('Введите число, с которого начать отсчет: '))
b = int(input('Введите число, на котором следует закончить: '))
# Цикл, который выводит числа в заданном диапазоне:
for el in count(a):
    if el > b:
        break
    else:
        print(el)

print('Второй цикл')
c = input('Введите строку, которую следует повторять: ')
d = int(input('Введите количество символов, которое следует повторить: '))
# Цикл, который повторяет заданную строку до достижения заданного количества символов:
e = 0
for i in cycle(c):
    if e > d:
        break
    else:
        print(i)
        e += 1
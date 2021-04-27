print('Задача 7.')

from math import factorial

num = int(input('Введите число: '))

print('Факториал всех чисел, входящих в ваше число:')

def fact(num):
    """
    Функция возвращает факториал всех целых чисел в составе введенного числа:
    :param num: Введенное пользователем число
    :yield: Генератор факториала введенного числа
    """
    for i in range(num):
        print(f'!{i + 1} =', factorial(i + 1))
    c = factorial(num)
    yield c

for el in fact(num):
    print('Факториал вашего числа:')
    print(f'!{num} =', el)


print('Задача 5.')

from functools import reduce

a = 100
b = 1000
print(f'Диапазон {a}-{b}')
# Цикл выбирает все четные значения в заданном диапазоне:
list = [i for i in range(a, b) if i % 2 == 0]

def func(prev_el, el):
    """
    Функция возвращает произведение всех элементов заданного списка:
    :param prev_el: Предыдущий элемент
    :param el: Следующий элемент
    :return: Произведение
    """
    return prev_el * el

print('Произведение всех элементов диапазона:')
print(reduce(func, list))
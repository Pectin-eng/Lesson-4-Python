print('Задача 1.')

hours = int(input('Введите количество отработанных сотрудником часов: '))
dollars = int(input('Введите почасовую ставку: '))
prize = int(input('Введите размер премии: '))

def my_func(hours, dollars, prize):
    """
    Функция возвращает расчет заработной платы сотрудника согласно введенной формуле:
    :param hours: Часы выработки
    :param dollars: Ставка за час
    :param prize: Премия
    :return: Формула расчета заработной платы
    """
    return (hours * dollars) + prize

print('Заработная плата сотрудника:', my_func(hours, dollars, prize))

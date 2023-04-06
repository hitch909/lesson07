'''Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход).'''


class Worker:
    name = 'Наполеон'
    surname = 'Бонапарт'
    position = 'император'
    __income = {"wage": 1000, "bonus": 500}

    class Position:
        def __str__(self, name, surname, patronymic):
            print(f'{name}  {surname}  {patronymic}')

        def __init__(self, get_total_income):
            self.get_total_income = get_total_income

    patronymic = 'Карло'

    get_total_income = Position('')
    get_total_income = sum(__income.values())
    print(f'доход с учетом премии = {get_total_income}')

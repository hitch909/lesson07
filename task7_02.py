'''
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
'''


class Road:
    weight = 25
    thickness = 0.01

    def __init__(self, length, width):
        self.__length__ = length
        self.__width__ = width

    def calculation(self, weight, thickness, length, width):
        result = weight * thickness * length * width
        return result


kl_road = Road(5000, 20)

print(kl_road.calculation(25, 0.01, 5000, 20))

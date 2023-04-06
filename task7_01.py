# # Задание 1.
#
# # Создать класс TrafficLight (светофор)
# # и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

import time

class TrafficLight:
    '''описание работы светофора'''
    __color = ''

    def col(self, red, yellow, green):
        self.rad = red
        self.yellow = yellow
        self.green = green

    '''запуск светофора'''

    def running(self, col):
        while True:
            print("\033[31m {}".format(Traffic_Light.rad))
            time.sleep(5)
            print("\033[33m {}".format(Traffic_Light.yellow))
            time.sleep(2)
            print("\033[32m {}".format(Traffic_Light.green))
            time.sleep(3)
    '''не знаю как реализовать остановку по команде )))'''


Traffic_Light = TrafficLight()
Traffic_Light.col('красный', 'желтый', 'зеленый')
Traffic_Light.running('col')


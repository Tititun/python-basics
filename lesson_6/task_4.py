# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

from random import choice

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение! Ваша скорость {self.speed}, максимальная - 60')
        else:
            print(self.speed)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение! Ваша скорость {self.speed}, максимальная - 40')
        else:
            print(self.speed)

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def double_speed(self):
        self.speed *= 2
        print(self.speed)

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

Car_1 = TownCar(100, 'green', 'Audi')
print(Car_1.speed)
print(Car_1.color)
print(Car_1.name)
print(Car_1.is_police)
Car_1.go()
Car_1.turn('налево')
Car_1.stop()
Car_1.show_speed()

Car_2 = SportCar(130, 'red', 'Ferrari')
Car_2.double_speed()

Car_3 = WorkCar(30, 'white', 'Gazel')
print(Car_3.name)

Car_4 = PoliceCar(70, 'blue', 'VW')
print(Car_4.is_police)

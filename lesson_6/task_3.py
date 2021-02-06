# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным
# и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}
# . Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).



class Worker:
    def __init__(self, name, surname, position, money):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = money

class Position(Worker):
    def __init__(self, name, surname, position, money):
        super().__init__(name, surname, position, money)

    def get_full_name(self):
        print(self.name, self.surname)
    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])

money = {
    'wage': 10000,
    'bonus': 500,
}

Driver = Position('Petr', 'Petrov', 'Driver', money)

print(Driver.name, Driver.surname, Driver.position)
Driver.get_full_name()
Driver.get_total_income()

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


from lesson_8.task_4 import Printer, Xerox, Scanner

class WareHouseError(Exception):
    pass

class Warehouse:
    def __init__(self):
        self.departments = {}

    def add_item(self, item, number, department):
        try:
            if type(number) != int:
                raise WareHouseError('необходимо ввести число отправляемых предметов')
            elif item.__class__ not in (Printer, Xerox, Scanner):
                raise WareHouseError('На склад принимается только оргтехника')
            elif department not in self.departments:
                self.departments[department] = []
            for i in range(number):
                self.departments[department].append(item)
        except WareHouseError as e:
            print(e)


myWarehouse = Warehouse()
myWarehouse.add_item(Printer('samsung'), 2, 'отдел кадров')
myWarehouse.add_item(Printer('samsung'), 'два', 'отдел кадров')
myWarehouse.add_item(Xerox('samsung'), 1, 'бухгалтерия')
myWarehouse.add_item('яблоко', 20, 'бухгалтерия')
myWarehouse.add_item(Scanner('hp'), 1, 'бухгалтерия')

print(myWarehouse.departments)

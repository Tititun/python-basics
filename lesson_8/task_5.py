# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на
# склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.


from lesson_8.task_4 import Printer, Xerox, Scanner

class Warehouse:

    def __init__(self):
        self.departments = {}

    def add_item(self, item, depatment):
        if depatment in self.departments:
            self.departments[depatment].append(item)
        else:
            self.departments[depatment] = []
            self.departments[depatment].append(item)


myWarehouse = Warehouse()
myWarehouse.add_item(Printer('samsung'), 'отдел кадров')
myWarehouse.add_item(Xerox('LG'), 'бухгалтерия')
myWarehouse.add_item(Scanner('Xiaomi'), 'бухгалтерия')

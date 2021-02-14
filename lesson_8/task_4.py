# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)


class Orgtech:
    size = 'size is big'
    price = 'price is high'

    def __init__(self, brand):
        self.brand = brand


class Printer(Orgtech):
    purpose = 'printing'

    def print_a_list(self):
        return 'напечатал лист'
    def __repr__(self):
        return f'принтер {self.brand}'

class Scanner(Orgtech):
    purpose = 'scanning'
    def __repr__(self):
        return f'сканер {self.brand}'


class Xerox(Orgtech):
    purpose = 'making copies'
    def __repr__(self):
        return f'ксерокс {self.brand}'


if __name__ == '__main__':      # некоторые из приведенных здесь классов используются в задании 5, поэтому
    my_warehouse = Warehouse()  # добавил эту строку
    my_warehouse.add_item(Printer('samsung'))
    my_warehouse.add_item(Scanner('hp'))
    my_warehouse.add_item(Xerox('LG'))

    for thing in my_warehouse.items:
        print(thing.size, thing.price, thing.purpose)

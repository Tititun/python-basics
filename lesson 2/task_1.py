# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

items = [30, 'apple', 0.22, None, True, {'money': 200, 'daytime': 'morning'}, [1, 2, 3]]

for item in items:
    print(type(item))

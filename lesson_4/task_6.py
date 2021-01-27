# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

from itertools import count, cycle

def iter_1(start_number, size):
    for num in count(start_number):
        yield num
        if num == size + start_number - 1:
            break

items = ['A', 'B', 'C', 'D']

def repeater(sequence, total_elements):
    i = 0
    for el in cycle(sequence):
        yield el
        i += 1
        if i == total_elements:
            break

for i in repeater(items, 10):
    print(i)

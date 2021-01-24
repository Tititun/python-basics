# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(first, second, third):
    numbers = [first, second, third]
    numbers.remove(min(numbers))
    return sum(numbers)

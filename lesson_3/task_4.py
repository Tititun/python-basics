# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

number_1 = float(input('Введите действительное положительное число:\n'))
number_2 = int(input('Введите целое отрицательное число:\n'))


# первый способ
def my_func(x, y):
    return x**y

# второй способ
# def my_func(x, y):
#     divisor = x
#     for i in range(abs(y)-1):
#         divisor *= x
#         i += 1
#     return 1 / divisor

print(my_func(number_1, number_2))
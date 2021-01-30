# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

number_1 = float(input('Введите делимое:\n'))
number_2 = float(input('Введите делитель:\n'))

def division(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        return 'Делить на ноль нельзя'

print(division(number_1, number_2))

# Другой вариант функции:

# def division(number1, number2):
#     try:
#         return number1 / number2
#     except ZeroDivisionError:
#         return 'Делить на ноль нельзя'

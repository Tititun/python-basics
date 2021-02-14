# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class ZeroDivisionError(Exception):
    def __init__(self, text):
        self.text = text

number = 100
div = int(input('Введите делитель для числа 100:\n'))

try:
    if div == 0:
        raise ZeroDivisionError('На ноль делить нельзя')
    result = number / div
    print(result)

except ZeroDivisionError as e:
    print(e)

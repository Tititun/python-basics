# Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
# типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

import re

class Date:
    def __init__(self, date_string):
        self.date = date_string

    @classmethod
    def string_to_num(cls, date):
        match = re.findall(r'\d+', date)
        if match:
            day, month, year = match
            return int(day), int(month), int(year)
        else:
            print('Неправильный формат даты')

    @staticmethod
    def validate_date(date):
        matches = re.findall(r'\d+', date)
        matches = map(int, matches)
        day, month, year = matches
        mistakes = []
        if day < 1 or day > 31:
            mistakes.append('День должен быть в пределах от 1 до 31')
        if month <1 or month > 12:
            mistakes.append('Месяц должен быть в пределах от 1 до 12')
        if len(str(year)) != 4:
            mistakes.append('Год должен содержать 4 цифры')
        if len(mistakes) == 0:
            return 'Формат даты верный'
        else:
            return mistakes

myDate = Date('12-11-2020')

print(Date.string_to_num('2-3-2019'))

print(myDate.validate_date(myDate.date))
print(myDate.validate_date('32-02-2002'))
print(myDate.validate_date('01-13-2002'))
print(myDate.validate_date('02-02-20022'))

# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.


def print_person(first_name='not specified', last_name='not specified',
           year='not specified', city = 'not_specified',
           email = 'not specified', phone_number='not_specified'):
    print(f'Имя: {first_name}, фамилия: {last_name}, год рождения: {year},'
          f' город проживания: {city}, email: {email}, телефон: {phone_number}.')


print_person(first_name='Иван', last_name='Иванов', year= 1955,
       city='Ярославль', email='ivan@ivan.com', phone_number=123456)

start_km = int(input('Введите число километров в первый день:\n'))
target_km = int(input('Введите желаемый результат:\n'))

day_number = 1
current_km = start_km  # можно и несоздавать новую переменную и использовать start_km, но по мне так читабельнее.

while current_km < target_km:
    current_km *= 1.1
    day_number += 1

print(f'Желаемый результат будет достигнут в день {day_number}.')
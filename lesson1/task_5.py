income = int(input('Введите выручку фирмы:\n'))
spendings = int(input('Введите издержки фирмы:\n'))

outcome = income - spendings
if outcome > 0:
    print('Вы работаете с прибылью.')
    if income > 0:
        print(f'Рентабельность составляет {outcome/income}')
        workers_number = int(input('Введите число сотрудников:\n'))
        print(f'Прибыль на одного сотрудника составляет: {round(outcome/workers_number)}')
elif outcome == 0:
    print('Вы работаете в ноль.')
else:
    print('Вы работаете в убыток.')

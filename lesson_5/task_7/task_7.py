# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка
# будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.


import json

with open('task_7_text.txt', encoding='utf8') as f:
    total = 0
    profitable_firms = 0
    firms = {}
    for line in f:
        firm, _, income, spendings = line.split()
        earnings = float(income) - float(spendings)
        if earnings > 0:
            total += earnings
            profitable_firms += 1
        firms[firm] = earnings
    profit = {'average_profit': round(total / profitable_firms, 2)}
    print(firms)
    print(profit)

with open('task_7.json', 'w', encoding='utf8') as o:
    json.dump([firms, profit], o, ensure_ascii=False)

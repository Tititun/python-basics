# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('task_3_text.txt', encoding='utf8') as f:
    lines = f.readlines()
    total_earnings = 0
    for line in lines:
        name, income = line.split()
        total_earnings += float(income)
        if float(income) < 20000:
            print(f'Сотрудник {name} получает меньше 20000 рублей ({income}).')
    print(f'Средний доход: {total_earnings / len(lines)}.')

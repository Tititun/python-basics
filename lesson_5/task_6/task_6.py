# Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


with open('task_6_text.txt', encoding='utf8') as f:
    subjects = {}
    for line in f:
        subject = line.split()[0][:-1]
        hours_with_brackets = [hour for hour in line.split()[1:]]
        total_hours = sum([int(hour.split('(')[0]) for hour in hours_with_brackets])
        subjects[subject] = total_hours
    print(subjects)
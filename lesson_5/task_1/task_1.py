# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.


with open('task_1_text.txt', 'w', encoding='utf8') as f:
    while True:
        line = input('Введите данные, оставьте строку пустой для выхода:\n')
        if line != '':
            f.writelines(line + '\n')
        else:
            print('Программа завершена.')
            break

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

eng_rus = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open('task_4_text.txt', encoding='utf8') as file_1:
    with open('task_4_output.txt', 'w', encoding='utf8') as file_2:
        for line in file_1:
            line_words = line.split()
            line_words[0] = eng_rus[line_words[0]]
            file_2.write(' '.join(line_words) + '\n')


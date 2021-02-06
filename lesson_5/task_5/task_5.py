# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint


with open('task_5_text.txt', 'w', encoding='utf8') as f:
    sequence = [randint(1, 11) for i in range(5)]
    print(f'Сумма чисел: {sum(sequence)}')
    f.write(' '.join([str(number) for number in sequence]))

# Если надо выполнить чтение отдельно:
# with open('task_5_text.txt', encoding='utf8') as f:
#     total = sum([int(number) for number in f.read().split()])
#     print(total)

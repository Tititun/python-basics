# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.


with open('task_2_text.txt', encoding='utf8') as f:
    counter = 1
    for line in f:
        print(f'число слов в строке {counter}: {len(line.split())}')
        counter += 1
    print(f'Число строк: {counter - 1}.')

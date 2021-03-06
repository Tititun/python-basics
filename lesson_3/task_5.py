# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

total = 0
special_symbol = False

while not special_symbol:
    user_input = input('Введите строку чисел, разделенных пробелом:\n')
    numbers = user_input.split()
    for number in numbers:
        try:
            total += float(number)
        except ValueError:
            print('Введен специальный символ. Программа завершается.')
            special_symbol = True
            break
    print(total)

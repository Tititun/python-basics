# Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов
# нужно использовать функцию input().

print('Введите новый элемент списка, для выхода введите q')

user_list = []
counter = 1
while True:
    item = input(f'Введите элемент {counter}:\n')
    if item == 'q':
        break
    else:
        user_list.append(item)
        counter += 1

for i in range(len(user_list)):
    if i % 2 == 0 and i != len(user_list) - 1:
        item_1 = user_list[i]
        item_2 = user_list[i + 1]
        user_list[i] = item_2
        user_list[i + 1] = item_1

print(user_list)
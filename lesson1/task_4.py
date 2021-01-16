number = int(input('Введите целое положительное число\n'))

largest_digit = 0

while number > 0:
    remained = number % 10
    if largest_digit < remained:
        largest_digit = remained
    number = int(number / 10)
print(largest_digit)

# Если честно, то долго думал, как сделать это только используя while и арифметику.
# В итоге не удержался и посмотрел подсказку в интернете.
# Сам бы я сделал это вот так:
# max([int(digit) for digit in str(number)])
# но мы это еще не проходили. поэтому пришлось помучиться.

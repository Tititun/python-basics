seconds = int(input('Введите время в секундах.\n'))
minutes = seconds // 60
hours = seconds // 3600
print(f'{hours}:{minutes}:{seconds}')
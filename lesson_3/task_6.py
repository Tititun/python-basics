# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
# и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

# простой способ с импользованием встроенной функции
def inc_func(text):
    return text.capitalize()

print(inc_func('doros'))

# витиеватый способ с использованием позиции буквы в юникоде
def inc_func(text):
    first_letter = text[0]
    first_letter_code = ord(first_letter)
    first_letter_capitalized = chr(first_letter_code-32)  # заглавные и маленькие латинские буквы отличаются
    text = first_letter_capitalized + text[1:]            # на 32 позиции в юникоде
    return text

print(inc_func('doros'))

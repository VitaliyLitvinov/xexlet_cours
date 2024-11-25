# Реализуйте функцию choice_from_range(),
# которая принимает строку-набор и возвращает
# случайный символ по индексу из ограниченного диапазона.

# Аргументы функции:

# строка-набор
# начальный индекс диапазона
# конечный индекс диапазона

from random import random, randint

text = "abcdef"
def choice_from_range(text, a, b):
    random_index = randint(a, b)
    char = text[random_index]
    print(char)
choice_from_range(text, 3, 5)  # d
choice_from_range(text, 3, 5)  # f
choice_from_range(text, 3, 5)  # e
choice_from_range(text, 2, 2)
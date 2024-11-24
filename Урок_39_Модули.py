# Реализуйте функцию count_vowels(), которая принимает строку,
# считает и возвращает количество гласных букв в ней.

# Для проверки, является ли буква гласной, импортируйте
# и используйте функцию is_vowel() из модуля symbols.py.

from symbols import is_vowel
def count_vowels(text:  str):
    sum = 0
    for i in text:
        if is_vowel(i) == True:
            sum += 1
        else:
            sum += 0
    return sum

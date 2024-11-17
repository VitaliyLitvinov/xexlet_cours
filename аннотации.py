#   Реализуйте функцию letter_multiply(). Она должна принимать три параметра:

#   Слово, тип данных строка
#   Букву, тоже строка, но состоящая из одного символа
#   Число, которое обозначает, сколько раз нужно повторить букву в слове
#       text = 'python'
#       print(letter_multiply(text, 'p', 2)) # => ppython
#       print(letter_multiply(text, 'y', 3)) # => pyyython
#       print(letter_multiply(text, 'n', 4)) # => pythonnnn
#   Функция должна возвращать строку — слово с повторенными символами

#   Укажите аннотации типов при объявлении функции.

text = 'pythyn'
def letter_multiply(word: str, letter: str, number: int) -> str:
    result: str = word.replace(letter, letter * number)
    return result

print(letter_multiply(text, 'p', 2))
print(letter_multiply(text, 'y', 3))
print(letter_multiply(text, 'n', 4))

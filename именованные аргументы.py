#Реализуйте функцию trim_and_repeat(), которая принимает три параметра:

#Строку
#offset — число символов, на которое нужно обрезать строку слева
#repetitions — сколько раз нужно повторить строку перед возвратом получившейся строки
#Число символов для среза по умолчанию равно 0, а количество повторений по умолчанию равно 1.

#Функция должна возвращать полученную строку.


text = 'python'
def trim_and_repeat(text, offset=0, repetitions=1):
    return text[offset:] * repetitions


print(trim_and_repeat(text, offset=3, repetitions=2))
#1
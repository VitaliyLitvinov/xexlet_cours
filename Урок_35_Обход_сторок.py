# Реализуйте функцию my_substr(),
# которая извлекает из строки подстроку указанной длины.
# Она принимает на вход два аргумента (строку и длину) и
# возвращает подстроку, начиная с первого символа:
string = 'If I look back I am lost'

def my_substr(string, lenght):
    index = 0
    substr = ''
    while index < lenght:
        substr += string[index]
        index += 1
    return substr
print(my_substr(string, 1))  # => 'I'
print(my_substr(string, 7))
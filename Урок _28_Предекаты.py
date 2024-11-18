#Реализуйте функцию has_upper_case(), которая определяет,
#содержит ли строка заглавные буквы. Функция должна вернуть булево значение:

def has_upper_case(text):
     print(text != text.lower())
#print(has_upper_case('sWd'))
has_upper_case('')  # False
has_upper_case('python')  # False
has_upper_case('pyThon')  # True
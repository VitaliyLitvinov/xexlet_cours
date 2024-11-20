# Реализуйте функцию string_or_not(),
# которая проверяет является ли переданный параметр строкой.
# Если да, то возвращается строка yes, иначе no.

def string_or_not(text: str):
    print ( isinstance(text, str) and 'yes' or 'no')
string_or_not('123')
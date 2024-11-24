# Реализуйте функцию has_char(). Она должна проверять,
# содержит ли строка указанную букву (вне зависимости от регистра).
# Функция принимает два параметра:

# Строка
# Буква для поиска
# И возвращает результат проверки – булево значение.

def has_char(text: str, char):
    index = 0
    while index < len(text):
        if text[index].upper() ==  char.upper():
            return True
            break
        index += 1
    return False

print(has_char('Hexlet', 'H'))  # => True
print(has_char('Hexlet', 'h'))  # => True
print(has_char('Awesomeness', 'd'))  # => False
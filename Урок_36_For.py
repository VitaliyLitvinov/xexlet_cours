# Реализуйте функцию filter_string().
# Она принимает на вход строку и символ и возвращает новую строку,
# в которой удален переданный символ во всех его позициях.
# Если строка не содержит указанный символ, то она возвращается без изменений.

# Итоговая строка также не должна содержать начальные и концевые пробелы:
# На этот раз реализуйте эту функцию с помощью цикла for.
# Дополнительное условие: регистр исключаемого символа не имеет значения.

def filter_string(string: str, symbol):
    result = ""
    for current_symbol in string.lower():
        if current_symbol.lower() != symbol.lower():
            result += current_symbol


    print(result.strip())
text = 'I look back if you are lost'

filter_string(text, 'i')  # 'look back f you are lost'
filter_string(text, 'O')  # 'I lk back if yu are lst'

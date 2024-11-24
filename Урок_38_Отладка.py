#Реализуйте функцию is_palindrome(), которая принимает на вход слово,
# определяет, является ли оно палиндромом,
# а затем возвращает логическое значение.
def is_palindrome(text: str):
    if text[::-1].lower() == text.lower():
        return True
    else:
        return False
print(is_palindrome(""))
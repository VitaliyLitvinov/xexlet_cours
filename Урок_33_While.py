# Напишите функцию print_numbers(). Функция должна принимать число и
# выводить числа в обратном порядке от этого числа до нуля (нуль не выводится).
#
# По окончании работы функция должна вывести на экран строку finished!.
def print_numbers(i: int):
    while i > 0:
        print(i)
        i -= 1
    print("finished!")
print_numbers(4)
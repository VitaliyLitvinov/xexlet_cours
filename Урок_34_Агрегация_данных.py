# Реализуйте функцию join_numbers_from_range(),
# которая объединяет все числа из диапазона в строку
# и возвращает получившуюся строку:

def join_numbers_from_range(start, finish):
    i = start
    sum = ' '
    while i <= finish:
        sum += str(i)
        i += 1
    print(sum)


join_numbers_from_range(5, 10)

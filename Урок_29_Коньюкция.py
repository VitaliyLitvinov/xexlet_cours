#Реализуйте функцию is_leap_year(), которая принимает год
#в качестве параметра и определяет, является ли этот год високосным.
#Функция должна вернуть True, если переданный год високосный и False, если нет.

#Год будет високосным, если он делится без остатка на 400,
#или он одновременно делится без остатка на 4 и не делится на 100:

def  is_leap_year(year):
    leap_year = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    print(leap_year)
is_leap_year(2017)


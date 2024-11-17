#   Напишите функцию get_age_difference(),
#   которая принимает два года рождения и возвращает строку
#   разницей в возрасте в виде The age difference is 11.

def get_age_difference(age1, age2):
    difference = age1 - age2
    return 'The age difference is ' + str(abs(difference))
actual = get_age_difference(2001, 2018)
print(actual)


#   Альтернативное решение
def get_age_difference(age1, age2):
    difference = age1 - age2
    if difference > 0:
       return 'The age difference is' + str(difference)
    else:
       difference1 = int(difference) * -1
       return 'The age difference is ' + str(difference1)
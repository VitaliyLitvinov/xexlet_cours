# Реализуйте функцию get_number_explanation(),
# которая принимает на вход число и возвращает объяснение этого числа.
# Если для числа нет объяснения, то возвращается just a number.
# Объяснения есть только для следующих чисел:

#  666 - devil number
#  42 - answer for everything
#  7 - prime number

def get_number_explanation(number: int):
    match number:
        case 666:
            print("devil number")
        case 42:
            print("answer for everything")
        case 7:
            print("prime number")
        case _:
            print("just a number")

get_number_explanation(8)  # just a number
get_number_explanation(666)  # devil number
get_number_explanation(42)  # answer for everything
get_number_explanation(7)  # prime number
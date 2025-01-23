'''
скрипт склоняет слово компьютер в щависимости орт ведённого числа
'''
def sklonenie(number):
    edinici = [2, 3, 4]
    desyatki = [12, 13, 14]
    sotni = [1012, 1013, 1014]

    if number % 10 == 1 and number % 100 != 11:
        return f"{number} компьютер"
    elif (number % 10 in edinici) and (number % 100 not in desyatki) :
        return f"{number} компьютера"
    else:
        return f"{number} компьютеров"

while True:

    user_inp = input()
    try:
        number = int(user_inp)
        result = sklonenie(number)
        print(result)
    except ValueError:
        print("введите корректное целое число.")

        #  and number % 100 != 11
    
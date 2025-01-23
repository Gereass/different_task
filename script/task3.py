'''
скрипт выводит массив простых чисел в диапазоне из диапазона
'''
def prostoe_chislo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prostoe_chislo_in_range(min_num, max_num):
    return [num for num in range(min_num, max_num + 1) if prostoe_chislo(num)]

user_input = input("введите 2 целых числа через пробел(интервал): ")
numbers = [int(num) for num in user_input.split(' ') if num.isdigit()]

result = prostoe_chislo_in_range(numbers[0], numbers[1])
print(result) 
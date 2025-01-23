'''
скрипт вычисляет общий длелителтель чисел массива
'''
def delitel(numbers):
    if not numbers:
        return []
    
    min_number = min(numbers)
    
    delitel_arr = []
    for i in range(1, min_number + 1):
        if min_number % i == 0:
            if all(num % i == 0 for num in numbers):
                delitel_arr.append(i)
    
    return delitel_arr


user_input = input("введите положительные целые числа через пробел: ")
numbers = [int(num) for num in user_input.split(' ') if num.isdigit()]

result = delitel(numbers)
print("Общие делители:", result)
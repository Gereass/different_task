'''
скрипт генерирует матрицу 3 на 3 из диапазона и ищет такую матрицу что бы произведение её строк было равно произведению столбцов
 не для програмной части
'''
import numpy as np
from itertools import permutations

# Исходный массив из 9 элементов
array = [i for i in range(3, 12)]


# Получаем все возможные перестановки массива
perm = permutations(array)

# Преобразуем каждую перестановку в матрицу 3x3 и выводим
for p in perm:
    matrix = np.array(p).reshape(3, 3)
    arr_str = [matrix[0], matrix[1], matrix[2]]
    arr_stolb = [matrix[:,0], matrix[:,1], matrix[:,2]]
    if np.prod(arr_str[0]) == np.prod(arr_stolb[0]) and np.prod(arr_str[1]) == np.prod(arr_stolb[1]) and np.prod(arr_str[2]) == np.prod(arr_stolb[2]):
        print(matrix)
        break

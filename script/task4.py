'''
скрипт выводит таблицу умножения
'''
def table_umn(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:3}", end=" ")
        print()

user_inp = input()
number = int(user_inp)
result = table_umn(number)
print(result)
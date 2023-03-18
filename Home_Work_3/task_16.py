# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

import random
list = int(input('Enters the number of array elements: '))
list_arr = []
for i in range(list):
    list_arr.append(random.randint(0, 10))
print(list_arr, end=' ')
print()
num = int(input('Enter the number: '))
res = len([i for i in list_arr if i == num])
print(f"-> {res}")
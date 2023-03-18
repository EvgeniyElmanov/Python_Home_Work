# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
list = int(input('Enters the number of array elements: '))
list_arr = []
for i in range(list):
    list_arr.append(random.randint(0, 10))
print(list_arr, end=' ')
print()
max_el = max(list_arr)
num = int(input('Enter the number: '))
for i in list_arr:
    if max_el > i > num:
        max_el = i
print(f"-> {max_el}")
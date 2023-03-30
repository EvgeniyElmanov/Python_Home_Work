'''
Задача 32: Определить индексы элементов массива (списка), значения которых
принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
больше заданного максимума)
'''
def list_arr(a, min_num, max_num):
    arr = []
    for i in range(len(a)):
        if min_num <= a[i] <= max_num:
            arr.append(a[i])
            arr.append([i])
    return arr

a = [1, 5, 8, 12, 13, 7, 10, 11, 15]
min_num = int(input())
max_num = int(input())
print(list_arr(a, min_num, max_num))

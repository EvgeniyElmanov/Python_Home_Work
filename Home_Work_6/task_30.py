"""
Задача 30:  Заполните массив элементами арифметической прогрессии. Её
первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""
def list_arr(a, d, n):
    res = []
    for i in range(n):
        res.append(a + i * d)
    return res

a = int(input())
d = int(input())
n = int(input())
print(list_arr(a, d, n))

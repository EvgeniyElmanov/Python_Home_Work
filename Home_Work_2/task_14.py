# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int(input('Enter of number: '))
result = 1
i = 0
while result <= num:
    print(result, end=" ")
    i += 1
    result = 2 ** i

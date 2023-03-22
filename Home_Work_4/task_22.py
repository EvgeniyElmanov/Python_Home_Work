# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

set_1 = int(input('enter the number of elements of the first set: '))
set_2 = int(input('enter the number of elements of the second set: '))
m = set()
n = set()
for i in range(set_1):
    m.add(int(input(f"element {i}: ")))
print()
for i in range(set_2):
    n.add(int(input(f"element {i}: ")))
print(m)
print()
print(n)
res = m.intersection(n)
print()
print(f'output elements -> {sorted(res)}')
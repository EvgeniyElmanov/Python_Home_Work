# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

eagle = 0
tails = 0
i = 0
num_coins = int(input('Enter the number of coins -> '))
for i in range(num_coins):
    temp = int(input(f'coins {i} -> '))
    if temp == 0:
        eagle += 1
    if temp == 1:
        tails += 1
if eagle < tails:
    print(f'eagle -> {eagle}')
else:
    print(f'tails -> {tails}')

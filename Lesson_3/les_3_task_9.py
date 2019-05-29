# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

ROW = 10
COL = 10
arr = [[random.randint(0, 100) for _ in range(COL)] for _ in range(ROW)]
for row in arr:
    for i in row:
        print(f'{i:<3}', end='')
    print()
print('.............................................')
arr = list(zip(*arr))

min_arr = []
for row in arr:
    min = row[0]
    for item in row:
        if item <= min:
            min = item
    min_arr.append(min)

max = min_arr[0]
for item in min_arr:
    if item >= max:
        max = item

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы - {max}')

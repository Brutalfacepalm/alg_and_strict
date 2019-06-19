# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

len_arr = 50
arr = [random.randint(0, 1000) for _ in range(len_arr)]

min_i = 0
min = arr[min_i]
max_i = 0
max = arr[max_i]
for i, item in enumerate(arr):
    if item <= min:
        min = item
        min_i = i
    elif item > max:
        max = item
        max_i = i

print(arr)
arr[min_i], arr[max_i] = max, min
print(arr)

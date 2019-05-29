# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

len_arr = 10
arr = [random.randint(0, 100) for _ in range(len_arr)]
print(arr)
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
sum_ = 0
if max_i > min_i:
    for i in arr[min_i+1:max_i:]:
        sum_ += i
else:
    for i in arr[min_i-1:max_i:-1]:
        sum_ += i

print(f'Сумма элементов между минимальным и максимальным равна: {sum_}')
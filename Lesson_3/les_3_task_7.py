# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

len_arr = 50
arr = [random.randint(0, 100) for _ in range(len_arr)]
print(arr)

min_arr = []
for _ in range(2):
    min_i = 0
    min = arr[min_i]
    for i, item in enumerate(arr):
        if item <= min:
            min = item
            min_i = i
    min_arr.append(str(arr.pop(min_i)))

print('Два минимальных числа в массиве: {}'.format(", ".join(min_arr)))
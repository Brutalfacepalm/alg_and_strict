# 2. Во втором массиве сохранить индексы четных элементов первого массива.
import random

len_first_arr = 100

first_arr = [random.randint(1, 1000) for _ in range(len_first_arr)]
res_arr = [i for i, item in enumerate(first_arr) if item % 2 == 0]

print(first_arr)
print(res_arr)

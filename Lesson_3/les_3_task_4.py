# 4. Определить, какое число в массиве встречается чаще всего.

import random

len_arr = 100
arr = [random.randint(1, 20) for _ in range(len_arr)]
check_arr = list(set(arr))

max_count = 0
max_count_item = []
for index, item in enumerate(check_arr):
    count_i = arr.count(item)
    if count_i > max_count:
        max_count_item = []
        max_count = count_i
        max_count_item.append(str(item))
    elif count_i == max_count:
        max_count_item.append(str(item))
print(arr)
print('Число {} встречается в массиве чаще всего ({} раз).'.format(", ".join(max_count_item), max_count) if len(max_count_item) == 1 else 'В массиве нет наиболее часто встречающегося числа.')
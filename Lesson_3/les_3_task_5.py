# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random

len_arr = 50
arr = [random.randint(-100, 100) for _ in range(len_arr)]

check_arr = list(set([i for i in arr if i < 0]))
print(arr)
print(check_arr)
max_min = check_arr.pop()
while check_arr:
    check_num = check_arr.pop()
    if check_num > max_min:
        max_min = check_num

print(f'Максимальное минимально число - {max_min}')
# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

arr = [i for i in range(2, 100)]

dlm = {d: len([i for i in arr if i % d == 0]) for d in range(2, 10)}

for key, value in dlm.items():
    print(f'Для числа {key} в списке чисел от 2 до 99 имеется {value} делимых.')
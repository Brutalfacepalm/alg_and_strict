# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введиче длину ряда: '))
summ = 0

for sqrt in range(n):
    s = (-0.5)**sqrt
    summ += s

print(summ)
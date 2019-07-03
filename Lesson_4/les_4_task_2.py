# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

stop = int(input('Введите искомое по счету простое число: '))


# решето Ератосфена обычное
# "les_4_task_2.sieve(50)"
# 100 loops, best of 3: 185 usec per loop
# "les_4_task_2.sieve(500)"
# 100 loops, best of 3: 3.21 msec per loop
# "les_4_task_2.sieve(5000)"
# 100 loops, best of 3: 59.7 msec per loop
# "les_4_task_2.sieve(50000)"
# 100 loops, best of 3: 596 msec per loop
# O(n*log(log(n)))
def sieve(stop):
    count = 1
    simple = 2
    while count < stop:
        a = 0
        z = 2 * simple + 1
        arr = [i for i in range(a, z)]
        arr[0], arr[1] = 0, 0

        for num in arr:
            if num != 0:
                j = num * 2
                while j < z:
                    arr[j] = 0
                    j += num

        arr = [i for i in arr if i != 0]
        if len(arr) >= stop:
            arr = arr[:stop:]

        simple = max(arr)
        count = len(arr)
    return simple


# поиск в цикле
# "les_4_task_2.not_sieve(50)"
# 100 loops, best of 3: 406 usec per loop
# "les_4_task_2.not_sieve(500)"
# 100 loops, best of 3: 62.8 msec per loop
# "les_4_task_2.not_sieve(5000)"
# 100 loops, best of 3: 12 sec per loop
# O(n*n*log(log(n)))
def not_sieve(stop):
    count = 1
    simple = 2
    arr = [simple]
    f = True
    while count < stop:
        can = simple + 1
        for i in range(2, can):
            if can % i == 0:
                f = False
                break
        if f == True:
            arr.append(can)
        f = True
        simple = can
        count = len(arr)
    return simple


# решето Ератосфена улучшенное
# "les_4_task_2.sieve_m(50)"
# 100 loops, best of 3: 157 usec per loop
# "les_4_task_2.sieve_m(500)"
# 100 loops, best of 3: 2.17 msec per loop
# "les_4_task_2.sieve_m(5000)"
# 100 loops, best of 3: 39.2 msec per loop
# "les_4_task_2.sieve_m(50000)"
# 100 loops, best of 3: 397 msec per loop
# O(n*log(log(n)))
def sieve_m(stop):
    count = 1
    simple = 2
    while count < stop:
        a = 0
        z = simple * 2 + 1
        arr = [i for i in range(a, z)]
        arr[0], arr[1] = 0, 0
        for num in arr:
            if num ** 2 < z:
                if num != 0:
                    j = num ** 2
                    while j < z:
                        arr[j] = 0
                        if num != 2:
                            j += 2 * num
                        else:
                            j += num
            else:
                break
        arr = [i for i in arr if i != 0]
        if len(arr) >= stop:
            arr = arr[:stop:]
        simple = max(arr)
        count = len(arr)
    return simple


print(f'Искомое по счету простое число - {sieve(stop)}')
print(f'Искомое по счету простое число - {not_sieve(stop)}')
print(f'Искомое по счету простое число - {sieve_m(stop)}')

# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

s = int(input('Введите количество чисел: '))
num = ''
for i in range(s):
    n = input(f'Введите число номер {i+1}: ')
    num += n
n_search = int(input('Введите искомую цифру: '))
count = 0
num = int(num)


def search(num, count, n_search):
    if num:
        if num % 10 == n_search:
            count += 1
        else:
            pass
        count = search(num // 10, count, n_search)
        return count
    else:
        return count


res = search(num, count, n_search)

print(res)

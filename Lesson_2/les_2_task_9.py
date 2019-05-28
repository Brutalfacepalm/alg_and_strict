# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))

s = 0
def search_max(num, s):
    if num < 10:
        return num
    else:
        s += num % 10 + search_max(num // 10, s)
        return s

s_1 = search_max(num_1, s)
s_2 = search_max(num_2, s)
s_3 = search_max(num_3, s)

max_num = max(s_1, s_2, s_3)

if max_num == s_1:
    print(f'Наибольшее число - {num_1}, сумма цифр - {max_num}')
elif max_num == s_2:
    print(f'Наибольшее число - {num_2}, сумма цифр - {max_num}')
else:
    print(f'Наибольшее число - {num_3}, сумма цифр - {max_num}')

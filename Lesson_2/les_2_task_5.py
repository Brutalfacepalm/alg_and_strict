# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

code = 32

while code < 128:
    s = ''
    for _ in range(10):
        if code < 128:
            s += f'{code:>4} - {chr(code):<5}'
            code += 1
    print(s)
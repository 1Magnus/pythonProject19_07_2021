# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить
# случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от
# 'a' до 'f' включительно.

import random

a = int(input('Введите целое число (начало диапазона): '))
b = int(input('Введите целое число (конец диапазона): '))

print(random.randint(a, b))

a = float(input('Введите число (начало диапазона): '))
b = float(input('Введите число (конец диапазона): '))

print(round(random.uniform(a, b), 3))

a = ord(input('Введите первый символ (начало диапазона): '))
b = ord(input('Введите второй символ (начало диапазона): '))

print(chr(random.randint(a, b)))

# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти. Примечание:
# Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи. Результаты
# анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.

# Задача № 1
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


import sys


def get_result(n):
    if len(str(n)) == 3:
        result = [int(str(n)[0]) + int(str(n)[1]) + int(str(n)[2]),
                  int(str(n)[0]) * int(str(n)[1]) * int(str(n)[2])]
        print(sys.getsizeof(result), type(result))
    return result


number = input('Введите целове трехзначное число: ')
print(f'Сумма = {get_result(number)[0]}, Произведение = {get_result(number)[1]}')

# Задача № 2

# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

print('Ведите две буквы латинского алфавита:')
c1 = input('Первая буква: ')
c2 = input('Вторая буква: ')

pc1 = ord(c1) - ord('a') + 1
pc2 = ord(c2) - ord('a') + 1
d = abs(pc2 - pc1 - 1)
print(sys.getsizeof(pc1), type(pc1))
print(sys.getsizeof(pc2))
print(sys.getsizeof(d))
print(f'Буква "{c1}" {pc1}-я в алфавите\n'
      f'Буква "{c2}" {pc2}-я в алфавите\n'
      f'Между ними {d} буквы')

# Задача № 3
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

a = [0] * 10
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            a[j] += 1
for i in range(len(a)):
    if a[i] != 0:
        print(f'Числу {i} кратны {a[i]} чисел')

print(sys.getsizeof(a), type(a))


# ОС - Windows 10 64 - разрядная, Python - 3.9
# Задача № 1
# Переменная result = 72 байта, небольшой словарь с двумя значениями.
# Задача № 2
# Переменные pc1, pc2, d равны 28 байт, это обычные Int.
# Задача № 3
# Переменная а = 136 байт словарь длинной 10 символов

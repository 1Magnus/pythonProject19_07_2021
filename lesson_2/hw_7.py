# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


n = int(input('Введите натуральное число: '))
a = n * (n + 1) // 2
s = 0
for i in range(1, n+1):
    s += i
print(f'1+2+...+{n} = {s} что в свою очередь равно {n}({n}+1)/2 = {a}. Верно!')

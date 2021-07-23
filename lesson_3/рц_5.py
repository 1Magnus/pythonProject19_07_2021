# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


import random

N = 10
a = [0] * N
c_max = c_min = 0
for i in range(N):
    a[i] = random.randint(-99, 99)
print(a)


b = []
for i in a:
    if i < 0:
        b.append(i)
print(f'Максимальное отрицательное цисло - {max(b)}')
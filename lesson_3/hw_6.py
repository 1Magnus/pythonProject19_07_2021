# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.

import random

N = 10
a = [0] * N
c_max = c_min = 0
for i in range(N):
    a[i] = random.randint(0, 99)
print(a)

print(f'Индекс максимального элемента - {a.index(max(a))}, минимального -{a.index(min(a))}')

b = []
if a.index(max(a)) > a.index(min(a)):
    b = a[a.index(min(a)):a.index(max(a))]
else:
    b = a[a.index(max(a)):a.index(min(a))]

c = b[1:len(b)-1]
print(c)

print('Сумма элементов, находящихся между минимальным и максимальным элементами - ', sum(c))
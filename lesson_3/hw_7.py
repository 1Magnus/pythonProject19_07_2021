# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба
# являться минимальными), так и различаться .

import random

N = 10
a = [0] * N
c_max = c_min = 0
for i in range(N):
    a[i] = random.randint(0, 99)
print(a)

a_min_2 = max(a)
a_min_1 = min(a)

for i in range(len(a)):
    if a[i] <= a_min_2 and i != a.index(a_min_1):
        a_min_2 = a[i]


print(a_min_1, a_min_2)


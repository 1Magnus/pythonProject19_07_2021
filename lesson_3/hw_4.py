# Определить, какое число в массиве встречается чаще всего

import random
'''
N = 10
a = [0] * N
c_max = c_min = 0
for i in range(N):
    a[i] = random.randint(1, 99)
print(a)
'''

z= b = 0
a = [1, 1, 1, 2, 2, 2, 2, 3]
for i in a:
    if a.count(i) > b:
        b = a.count(i)
        z = i

print(f'Число {z} встречаеться {b} раза.')
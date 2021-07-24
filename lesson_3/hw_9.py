# Найти максимальный элемент среди минимальных элементов столбцов матрицы
import random

random.seed(7)

N = 5
a = []
for str in range(N):
    b = []
    for row in range(N):
        b.append(random.randint(0, 99))
    a.append(b)

for i in range(N):
    print(a[i])

print('*' * 20)

d = []
for row in range(N):
    c = []
    for str in range(N):
        c.append(a[str][row])
    d.append(min(c))
    # print(c)

# print('*' * 20)
print(f'{d} - Минимальные элементы столбцов, из них максимальный {max(d)}')

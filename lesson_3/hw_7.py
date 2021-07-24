# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба
# являться минимальными), так и различаться .

import random


def rand_mass(N):
    a = [0] * N
    for i in range(N):
        a[i] = random.randint(1, 99)
    return a


def main():
    N = 10
    a = rand_mass(N)
    print(a, 'Оригинал')

    a_min_2 = max(a)
    a_min_1 = min(a)

    for i in range(len(a)):
        if a[i] <= a_min_2 and i != a.index(a_min_1):
            a_min_2 = a[i]

    print(f'Два минимальных числа равны - {a_min_1}, {a_min_2}')


if __name__ == '__main__':
    main()

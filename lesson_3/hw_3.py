
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random


def rand_mass(N):
    a = [0] * N
    for i in range(N):
        a[i] = random.randint(1, 99)
    return a


def main():
    N = 10
    a = rand_mass(N)
    print(a, '- Оригинал')
    # v1
    print('V1')
    c_max = c_min = 0
    for i in range(N):
        if a[i] > a[c_max]:
            c_max = i
        if a[i] < a[c_min]:
            c_min = i

    b = a[c_max]
    a[c_max] = a[c_min]
    a[c_min] = b
    print(a)

    # v2
    print('V2')
    a[a.index((max(a)))], a[a.index(min(a))] = a[a.index(min(a))], a[a.index((max(a)))]
    print(a)


if __name__ == '__main__':
    main()

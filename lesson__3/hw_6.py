# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.

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
    print(f'Индекс максимального элемента - {a.index(max(a))}, минимального - {a.index(min(a))}')

    b = []
    if a.index(max(a)) > a.index(min(a)):
        b = a[a.index(min(a)):a.index(max(a))]
    else:
        b = a[a.index(max(a)):a.index(min(a))]

    c = b[1:len(b)]
    print(c)

    print('Сумма элементов, находящихся между минимальным и максимальным элементами - ', sum(c))


if __name__ == '__main__':
    main()

# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


import random


def rand_mass(N):
    a = [0] * N
    for i in range(N):
        a[i] = random.randint(-99, 99)
    return a


def main():
    N = 10
    a = rand_mass(N)
    print(a)
    b = []
    for i in a:
        if i < 0:
            b.append(i)
    print(f'Максимальное отрицательное цисло - {max(b)} и его положение в масиве - {a.index(max((b))) + 1}')


if __name__ == '__main__':
    main()
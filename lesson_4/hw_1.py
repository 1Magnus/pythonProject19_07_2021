# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех
# уроков.

import random, cProfile


def rand_mass(N):
    a = [0] * N
    for i in range(N):
        a[i] = random.randint(1, 99)
    return a


def switch_el_1(a):
    print('V1')
    c_max = c_min = 0
    for i in range(len(a)):
        if a[i] > a[c_max]:
            c_max = i
        if a[i] < a[c_min]:
            c_min = i

    b = a[c_max]
    a[c_max] = a[c_min]
    a[c_min] = b
    return a


def switch_el_2(a):
    print('V2')
    a[a.index((max(a)))], a[a.index(min(a))] = a[a.index(min(a))], a[a.index((max(a)))]
    return a


def main():
    N = 1000000
    a = rand_mass(N)
    print(a, '- Оригинал')

    print(switch_el_1(a))

    print(switch_el_2(a))


if __name__ == '__main__':
    cProfile.run('main()')

# Вывод: операция перезначения сработала почти в два раза быстрее чем перебор всего списка. А также второй способ
# отрабатывает за одно и тоже время, что являеться еще одним плюсом.

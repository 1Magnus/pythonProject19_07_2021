# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках

import random


def get_median(user_list):
    for i in range(len(user_list)):
        left, right = [], []
        for j in range(len(user_list)):
            if i != j:
                if user_list[i] > user_list[j]:
                    left.append(user_list[j])
                else:
                    right.append(user_list[j])
        if len(left) == len(right):
            return user_list[i]


def get_median_sort(user_list):
    mid = len(user_list) // 2
    gap = len(user_list)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))
        swaps = False
        for i in range(len(user_list) - gap):
            j = i + gap
            if user_list[i] > user_list[j]:
                user_list[i], user_list[j] = user_list[j], user_list[i]
                swaps = True
    return user_list[mid]


def main():
    n = 4
    a = [random.randint(0, 100) for _ in range(2 * n + 1)]
    print(a, ' - оригинал')
    print(get_median(a), '- медиана без сортировки (сравнение)')
    print(get_median_sort(a), '- медиана с сортировкой расчёской')


if __name__ == '__main__':
    main()

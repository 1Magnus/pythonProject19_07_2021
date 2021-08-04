# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(list1):
    if len(list1) < 2:
        return list1
    else:
        mid = len(list1) // 2
        left = merge_sort(list1[:mid])
        right = merge_sort(list1[mid:])
        return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def main():
    n = 20
    a = [random.randint(0, 49) for _ in range(n)]
    print(a, ' - оригинал')
    print(merge_sort(a), ' - отсортированный')


if __name__ == '__main__':
    main()

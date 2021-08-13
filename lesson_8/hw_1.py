# Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

def get_slice(string):
    shag = 0
    simple = 1
    n = len(string)
    result = []
    while simple != n:
        for i in range(n - shag):
            result.append(string[i:i + simple])
        shag += 1
        simple += 1
    return result


def get_uni(list1):
    list2 = []
    result = []
    for i in list1:
        pass
        # функция подсчета кэша, добавляем в лист кэш, если кэша нет, добавляем ээлемент в результат
        z = 123
        if z not in list2:
            result.append(i)

    return result


def main():
    s = 'hello word'
    n = len(s)
    get_slice(s)


if __name__ == '__main__':
    main()

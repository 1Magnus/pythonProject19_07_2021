# Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
import hashlib


def get_slice(string):
    step = 0
    symbol = 1
    n = len(string)
    result = []
    while symbol != n:
        for i in range(n - step):
            result.append(string[i:i + symbol])
        step += 1
        symbol += 1
    return result


def get_uni(list1):
    list2 = []
    result = []
    for i in list1:
        z = hashlib.sha1(i.encode('utf-8')).hexdigest()
        if z not in list2:
            list2.append(z)
            result.append(i)
    return result


def main():
    s = 'koka'

    print(get_slice(s), '- все возможные комбинации')
    print(get_uni(get_slice(s)), '- уникальные комбинации')


if __name__ == '__main__':
    main()

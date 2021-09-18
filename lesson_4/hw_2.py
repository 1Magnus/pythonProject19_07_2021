# Написать два алгоритма нахождения i-го по счёту простого числа. Без использования «Решета Эратосфена»; Используя
# алгоритм «Решето Эратосфена» Примечание ко всему домашнему заданию: Проанализировать скорость и сложность
# алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
import cProfile


def i_nat_numb_ert(elem, n=10000000):
    a = [i for i in range(n)]
    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0
    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j += m  # перейти в позицию на m больше
        m += 1

    b = []
    for i in a:
        if i > 0:
            b.append(i)

    return b[elem - 1]


def i_nat_numb_not_ert(elem, n=10000000):
    lst = []
    count_elem = 0
    for i in range(2, n + 1):
        if count_elem <= elem:
            for j in lst:
                if i % j == 0:
                    break
            else:
                lst.append(i)
                count_elem += 1
        else:
            break
    return lst[elem - 1]


def main():

    z = int(input("Укажите порядковый номер простого числа: "))
    print(f'Используя алгоритм «Решето Эратосфена» i = {i_nat_numb_ert(z)}')
    print(f'Не используя алгоритм «Решето Эратосфена» i = {i_nat_numb_not_ert(z)}')


if __name__ == '__main__':
    cProfile.run('main()')

# Вывод: "Алгоритм без решето срабатывает быстее за счет того что останавливает генерацию на i-ом элементе"
'''
"C:\Program Files\Python39\python.exe" C:/pythonProject19_07_2021/lesson_4/hw_2.py
Укажите порядковый номер простого числа: 1000
Используя алгоритм «Решето Эратосфена» i = 7919
Не используя алгоритм «Решето Эратосфена» i = 7919
         665593 function calls in 9.388 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    9.388    9.388 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
        1    0.029    0.029    0.029    0.029 hw_2.py:29(i_nat_numb_not_ert)
        1    0.098    0.098    9.388    9.388 hw_2.py:45(main)
        1    4.890    4.890    5.540    5.540 hw_2.py:7(i_nat_numb_ert)
        1    0.580    0.580    0.580    0.580 hw_2.py:8(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    9.388    9.388 {built-in method builtins.exec}
        1    3.721    3.721    3.721    3.721 {built-in method builtins.input}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
   665580    0.070    0.000    0.070    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



Process finished with exit code 0
'''
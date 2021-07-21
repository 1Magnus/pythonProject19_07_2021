# По введенным пользователем координатам двух точек вывести уравнение
# прямой вида y=kx+b
# проходящей через эти точки.

print('Введите координаты первой точки: ')
x1 = int(input('x1 = '))
y1 = int(input('y1 = '))

print('Введите координаты второй точки: ')
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

try:
    k = (y1 - y2) / (x1 - x2)
except ZeroDivisionError:
    k = 0


b = y2 - k * x2
print(f'Уравнение прямой проходящей через эти точки выглядит так y = {k}x + {b}')
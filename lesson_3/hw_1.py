# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

a = [0]*10
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            a[j] += 1
for i in range(len(a)):
    if a[i] != 0:
        print(f'На число {i} деляться {a[i]} числа')

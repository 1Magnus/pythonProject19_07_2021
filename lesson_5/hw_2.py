# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’,
# ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’,
# ‘E’]. Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections


def my_dex(list_hex):
    dex = 0
    list_hex_copy = list_hex.copy()
    list_hex_copy.reverse()
    for i in range(len(list_hex_copy)):
        dex += dex_table.get(list_hex_copy[i]) * (16 ** i)
    return dex


def my_hex(dex_num):
    result = []
    while dex_num > 16:
        a = dex_num % 16
        z = dex_num // 16
        result.append(a)
        dex_num = z
    else:
        result.append(z)
    result.reverse()
    b = []
    for i in range(len(result)):
        z = hex_table.get(result[i])
        b.append(z)
    return b


dex_table = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
             'D': 13, 'E': 14, 'F': 15}
hex_table = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
             11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def main():
    # Ввод чисел в 16
    num_1 = list(input('Вводим первое число: ').upper())
    num_2 = list(input('Вводим второе чило: ').upper())
    print('Числа - ', num_1, 'и', num_2)

    # Перевод и создание новых переменных в 10
    num_1_dex = my_dex(num_1)
    num_2_dex = my_dex(num_2)

    # Подсчет в 10 и перевод в 16
    print(f'Сумма чисел {num_1} + {num_2} = {my_hex(num_1_dex + num_2_dex)}')
    print(f'Произведение чисел {num_1} * {num_2} = {my_hex(num_1_dex * num_2_dex)}')


if __name__ == '__main__':
    main()

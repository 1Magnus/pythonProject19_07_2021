# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

def get_result(n):
    if len(str(n)) == 3:
        result = [int(str(n)[0]) + int(str(n)[1]) + int(str(n)[2]),
                  int(str(n)[0]) * int(str(n)[1]) * int(str(n)[2])]
    return result


def main():

    number = input('Введите целове трехзначное число: ')
    print(f'Сумма = {get_result(number)[0]}, Произведение = {get_result(number)[1]}')


if __name__ == '__main__':
    main()

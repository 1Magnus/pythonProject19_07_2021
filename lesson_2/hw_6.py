# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число

import random
n = random.randint(0, 100)
c = 1
print('Давай сыграем в игру, угадай число от 0 до 100')
while c <= 10:
    a = int(input('Попытка № ' + str(c) + ' : '))
    if a > n:
        print('Загаданное число меньше выбранного')
    elif a < n:
        print('Загаданное число больше выбранного')
    else:
        print(f'Ура поздравляю! тебе хватило {c} попыток что бы угадать!')
        break
    c += 1
else:
    print(f'Не повезло, загаданное число - {n}, следующий раз попробуй делить доступный диапазон на 2 и назыать середнее число.')
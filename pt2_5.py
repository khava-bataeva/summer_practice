import random

n = 0
k = ''
while '000' not in k:
    a = int(input('Орёл-0 или решка-1: '))
    i = random.randint(0, 1)
    if a == 1 or a == 0:
        if i == a:
            k += '1'
            print('Выиграл')
            print('Число выигрышей: ', k.count('1'),
                  'Число проигрышей: ', k.count('0'))
        else:
            k += '0'
            print('Проиграл')
            print('Число выигрышей: ', k.count('1'),
                  'Число проигрышей: ', k.count('0'))
    else:
        break
print('Игра завершена')

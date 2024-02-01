from random import randint
rand = randint(0, 100)
guess = int(input('Угадайте число от 0 до 100  '))
flag = True
number = 0
while flag:
    if guess > rand:
        print ('Ваше число больше того, что загадано')
        guess = int(input(f'Ещё попытку...  '))
        number += 1
    elif guess < rand:
        print('Ваше число меньше того, что загадано')
        guess = int(input(f'Ещё попытку...  '))
        number += 1
    else:
        print('Отличная интуиция! Вы угадали число :)')
        number += 1
        print(f'Всего попыток: {number}.')
        flag = False


import random

lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
punctuation = '!#$%&*+-=?@^_'


def greeting():
    print('Приветствую вас!!!')
    print('Я могу помочь вам составить безопасный пароль по вашим параметрам\n\n')


def forming_charlist():
    charlist = ''
    counter = 0
    if input('Включать ли цифры в пароль?(да, нет)\n') == 'да':
        charlist += digits
    if input('Включать ли строчные буквы в пароль?(да, нет)\n') == 'да':
        charlist += lowercase_letters
    if input('Включать ли заглавные буквы в пароль?(да, нет)\n') == 'да':
        charlist += uppercase_letters
    if input('Включать ли знаки пунктуации в пароль?(да, нет)\n') == 'да':
        charlist += punctuation
    if input('Исключать ли неоднозначные символы (il1Lo0O)?\n') == 'да':
        for c in 'il1Lo0O':
            charlist = charlist.replace(c, '')

    if charlist:
        return charlist
    else:
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print('Вы ничего не выбрали. Так нормального пароля не получится. Давайте еще раз')
        return forming_charlist()


def creating_password(charlist, length):
    password = ''
    for _ in range(length):
        password += random.choice(charlist)
    return password


def getting_count_and_length():
    times = int(input('Сколько вам нужно паролей?\n'))
    if times == 1:
        length = int(input('Какой длины должен быть ваш пароль?\n'))
        return times, length
    elif 1 < times < 1000:
        length = int(input('Какой длины должны быть ваши пароли?\n'))
        return times, length
    else:
        print('Что-то пошло не так. Имейте ввиду, что реализуемая длина пароля менее 1000 символов')
        return getting_count_and_length()


# Генератор паролей
password_list = []

greeting()
times, length = getting_count_and_length()
charlist = forming_charlist()

for _ in range(times):
    password_list.append(creating_password(charlist, length))
print('Держите ваши пароли:\n')
print(*password_list, sep='\n')
input()

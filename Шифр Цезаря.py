from time import sleep


def greeting():
    print('Здравствуйте, добро пожаловать в программу "Шифровальную машину"')
    print('Используется шифр Цезаря\n\n')


def get_parameters():
    exeption = '\n\n\n\n\n\n\n\n\nВы ввели некорректные значения. Начните ввод сначала'

    print('Учтите, что кодирование происходит в правую сторону, а декодирование - в левую')
    working_item = input('Вы хотите кодировать или декодировать сообщение(введите "кодировать" или "декодировать)"\n')
    if working_item == 'кодировать':
        code_or_decode = 2
    elif working_item == 'декодировать':
        code_or_decode = 1
    else:
        print(exeption)
        return get_parameters()

    working_item = input(
        'Сообщение на каком языке нужно кодировать/декодировать?(введите "русский" или "английский")\n')
    if working_item == 'русский':
        language = 32
    elif working_item == 'английский':
        language = 26
    else:
        print(exeption)
        return get_parameters()

    working_item = input('Какой шаг вы хотите использовать?\n')
    if working_item.isdigit() and (int(working_item) <= language):
        step = int(working_item)
    else:
        print('Длина шага не может быть больше длины алфавита(для русского 32 символа, для английского - 26)')
        sleep(2)
        print(exeption)
        return get_parameters()
    return code_or_decode, language, step


def normalize_view(language, num_char):
    if language == 32:
        if num_char > 1103:
            num_char -= 32
        elif num_char < 1072:
            num_char += 32
    elif language == 26:
        if num_char > 122:
            num_char -= 26
        elif num_char < 97:
            num_char += 26
    return num_char


def enigma(code_or_decode, language, step):
    print('Параметры приняты. Идет запуск Энигмы')
    sleep(3)
    print('"Энигма" запущена')
    message = list(input('Введите значение вашего сообщения\n'))

    for i in range(len(message)):

        capital = False
        char_from_message = message[i]

        if char_from_message.isalpha():
            if char_from_message.isupper():
                capital = True
                char_from_message = char_from_message.lower()
            char_from_message = ord(char_from_message) + (-1) ** code_or_decode * step
            char_from_message = chr(normalize_view(language, char_from_message))

            if capital:
                char_from_message = char_from_message.upper()

            message[i] = char_from_message

    return ''.join(message)


# Шифр Цезаря
greeting()
code_or_decode, language, step = get_parameters()
reformated_message = enigma(code_or_decode, language, step)

print(reformated_message)
input()


import random

alfabet = {'А': '*  --',
           'Б': '--  --  --  *',
           'В': '*  --  --',
           'Г': '--  --  *',
           'Д': '--  *  *',
           'Е': '*',
           'Ж': '*  *  *  --',
           'З': '--  --  *  *',
           'И': '*  *',
           'Й': '*  --  --  --',
           'К': '--  *  --',
           'Л': '*  --  *  *',
           'М': '--  --',
           'Н': '--  *',
           'О': '--  --  --',
           'П': '*  --  --  *',
           'Р': '*  --  *',
           'С': '*  *  *',
           'Т': '--',
           'У': '*  *  --',
           'Ф': '*  *  --  *',
           'Х': '*  *  *  *',
           'Ц': '--  *  --  *',
           'Ч': '--  --  --  *',
           'Ш': '--  --  --  --',
           'Щ': '--  --  *  --',
           'Ъ': '*  --  --  *  --  *',
           'Ы': '--  *  --  --',
           'Ь': '--  *  *  --',
           'Э': '*  *  *  --  *  *  *',
           'Ю': '*  *  --  --',
           'Я': '*  --  *  --'
           }

reversed_alfabet = {v: k for k, v in alfabet.items()}
reversed_game = False
i = 0
_i = 0

print('Let\'s learn the Morze alfabet.')

try:
    while True:
        liter = random.choice(list(alfabet.keys()))
        symbol = alfabet[liter]
        users_symbol = input(f'What is it {liter}, write here:\t')

        if symbol == users_symbol:
            print('Yes, you are so cool')
            i += 1
        elif users_symbol == 'reverse':
            reversed_game = True
            break
        elif users_symbol == '0':
            break
        else:
            print('No, you had a mistake')
            _i += 1

        continue

    while reversed_game:
        symbol = random.choice(list(alfabet.values()))
        liter = reversed_alfabet[symbol]
        users_liter = input(f'What is it {symbol}, write here:\t')

        if liter == users_liter:
            print('Yes, you are so cool')
            i += 1
        elif users_liter == '0':
            break
        else:
            print('No, you had a mistake')
            _i += 1

        continue

    print(f'You was right {i} times, and had a mistake {_i} times')

except:
    print('Unknown error')

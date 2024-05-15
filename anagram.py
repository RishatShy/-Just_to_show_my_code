import random

WORDS = ('любовь', 'счастье', 'удача')  # you can put your words here

print('Let\'s play anagram')

word = random.choice(WORDS)
REGULAR_WORD = word
mixed_word = ''

while word:
    position = random.randrange(len(word))
    mixed_word += word[position]
    word = word[:position] + word[(position + 1):]
print(mixed_word)

print('\tTry to guess what is that word')

while True:
    guess = input('\t\tWhat do you think (tap only Enter to stop)\n')
    if guess == REGULAR_WORD:
        print(f'You are right. It is {REGULAR_WORD}')
        break
    elif guess == '':
        break
    else:
        print('Try once again!')

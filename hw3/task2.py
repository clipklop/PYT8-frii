"""
    Task 2:

Напишите игру “Поле чудес”
Пример:
Начинаем играть: _ _ 
Введите букву: y
Есть такая буква! : y _ 
Введите букву: a
Нет такой буквы!
Введите букву: y
Такую букву уже называли!
Введите букву: p
Есть такая буква! : p y _ _
Введите букву: t
Есть такая буква! : p y t _ 
Введите букву: h
Есть такая буква! : p y t h _ _
Введите букву: o
Есть такая буква! : p y t h o _
Введите букву: n
Поздравляем, вы отгадали слово! : p y t h o n
"""
import random


WORDS = [
    'python', 'mango', 'tumeric', 'walnut'
]


def field_of_miracles(array: list):
    random.shuffle(array)
    correct = []
    wrong = []
    counter = 0
    score = 0
    print(f'Начинаем играть: ', end='')

    for word in array:
        string = '_' * len(word)
        print(string)

        while True:
            guess = input('\nВведите букву: ')

            if guess == '':
                print("\nOk, I'm out")
                break
            elif len(guess) != 1:
                print("Too many letters")
                continue
            elif guess in correct:
                print('Такую букву уже называли!')
                continue
            elif not guess.isalpha():
                print("Nope, only letters are allowed")

            if guess in word:
                correct.insert(word.index(guess), guess)
                string = string[:word.index(guess)] + guess + \
                    string[word.index(guess)+1:]
                print(f'\n{string}')
            else:
                wrong.append(guess)
                print(f"Нет такой буквы!: {' '.join(wrong)}", end=' ')
                print('\n' + string)

            if ''.join(correct).strip() == word:
                score += 1
                print(f"Correct! You've guessed {score} word of \
{len(array)} words")
                break

        correct = []
        counter += 1
        print(f'\nOk! Next word. {len(array) - counter} words left.')

    print(f'\nGood job! Your score is {score} words.')


field_of_miracles(WORDS)

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
    'python', 'avocado', 'tumeric', 'walnut'
]


def draw(guess, word):
    string = ''
    for letter in word:
        if letter in guess:
            #print(letter, end='')
            string += letter
            # print(string, end='')
        else:
            # print('_ ', end='')
            string += '_ '
#            print(stringend='')

    print('')
    return string


def field_of_miracles(array: list, guess: str):
    random.shuffle(array)
    correct = []
    counter = 0

    for word in array:
        print('_ ' * len(word))

        while True:
            guess = input('\nВведите букву: ')
            if guess in word:
                correct.append(guess)

            draw(guess, word)
            
            if ''.join(correct) == word:
                counter += 1
                print(f"Correct! You've guessed {counter} word of {len(array)} words")
                break

    print(f'Good job! Your score is {counter} words.')

            

field_of_miracles(WORDS, 'a')


def main():
    print('Начинаем играть: {}'.format(len()))
    guess = input('Введите букву: ')

    field_of_miracles(WORDS, guess)


#main()

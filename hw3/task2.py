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

WORDS = [
    'python', 'avocado', 'tumeric', 'walnut'
]


def field_of_miracles(array: list, guess: str):
    correct = []

    for word in array:
        print('_ ' * len(word))
        correct.append(guess) if guess in word else 0
field_of_miracles(WORDS, 'a')


def main():
    print('Начинаем играть: {}'.format(len()))
    guess = input('Введите букву: ')

    field_of_miracles(WORDS, guess)


#main()

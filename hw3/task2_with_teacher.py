#


QUIZ = 'Pythony'
GUESSED = []


def draw_word(guessed):
    for char in QUIZ:
        if char.lower() not in guessed:
            print('_', end=' ')
        else:
            print(char, end=' ')
    print()


def ask_user(guessed):
    new_char = input('Enter a letter: ').lower()
    if new_char in QUIZ.lower():
        if new_char not in guessed:
            print('Congratz, the letter is guessed!')
            guessed.append(new_char)
        else:
            print('You have already entered that letter.')
    else:
        print('Sorry, no such letter.')
    return guessed


def is_win(guessed):
    quiz = QUIZ.lower()
    for char in guessed:
        quiz = quiz.replace(char, '')
    return quiz == ''


while True:
    draw_word(GUESSED)
    GUESSED = ask_user(GUESSED)
    # if len(GUESSED) == len(QUIZ):
    #     print('You have won! Congratz!')
    #     break
    if is_win(GUESSED):
        print('You have won! Congratz!')
        break

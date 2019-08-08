""" 
    Task 1:

Напишите программу, которая проверяет, является ли введенная строка панграммой
(т.е. содержит все буквы либо русского, либо английской алфавита)
Пример русской панграммы - Широкая электрификация южных губерний даст мощный толчок подъёму сельского хозяйства.
Пример английской - The quick brown fox jumps over the lazy dog
Расширенный вариант - выводится, каких букв алфавита не хватает во фразе
"""

RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ENG = 'abcdefghijklmnopqrstuvwxyz'

ru_phrase = 'Широкая электрификация южных губерний даст мощный толчок подъёму сельского хозяйства'
eng_phrase = 'The quick brown fox jumps over the lazy dog'
insufficient_phrase = 'Размер паутины определяется только ее способностью ловить мух'


def check_alphabet(string, alphabet):
    right = []
    missing = []
    
    for char in alphabet:
        right.append(char) if char in string.lower() else missing.append(char)
    
    right_string = ''.join(sorted(set(right))).strip()
    missing_string = ''.join(sorted(set(missing))).strip()

    if len(right_string) == 26 or len(right_string) == 33:
        if alphabet == RU:
            right_string = right_string[:6] + right_string[-1] + right_string[6:-1]

        missing_string = 'Во фразе хватило всех букв'
        return right_string, len(right_string), alphabet == right_string, missing_string
    else:
        return right_string, len(right_string), alphabet == right_string, missing_string + ' букв не хватило во фразе'
        

print(check_alphabet(ru_phrase, RU))
print(check_alphabet(eng_phrase, ENG))
print(check_alphabet(insufficient_phrase, RU))

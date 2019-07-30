"""
    * A Quiz app

    Задание №1 (простое)
Написать программу, которая будет задавать пользователю вопросы, и проверять правильность ответов.
Если пользователь неправильно ответил на вопрос, то выводится сообщение, что ответ неверный и вопрос задается повторно.
Программа должна задавать не менее трех вопросов.
Вопросы задаются последовательно.
"""


questions = {
    'how many bits in one byte': 8,
    'how many patterns in one byte': 256,
    'how many characters could be stored in one byte': 1,
    'Whats name of Encoding system representing each typed character by a number': 'ASCII'
}


def quiz(array):
    return [x for x in array]


print(quiz(questions))





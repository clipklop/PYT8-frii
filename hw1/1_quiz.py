"""
    * A Quiz app
"""


questions = [
    ['how many bits in one byte', '8'],
    ['how many patterns in one byte', '256'],
    ['how many characters could be stored in one byte', '1'],
    ['Whats name of Encoding system representing each typed character by a \
number', 'ASCII']
]


def quiz(array):
    counter = 0
    while len(array) > counter:
        answer = input("{}: ".format(array[counter][0])).upper()
        if answer == array[counter][1]:
            counter += 1
    print('Congratz! You guessed all {} questions!'.format(counter))
    return


quiz(questions)

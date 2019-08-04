"""
    * A Quiz app on dicts
"""


questions = {
    'how many bits in one byte': '8',
    'how many bit patterns in one byte': '256',
    'how many characters could be stored in one byte': '1',
    'what is encoding system name that represents each character by a \
number': 'ascii',
    'specify one of the immutable data types in Python': [
        'int', 'float', 'bool', 'str', 'tuple']}


def quiz_dict(array):
    counter = 0
    for key, value in questions.items():
        while True:
            answer = input(f"{key}: ")
            print(answer)

            if answer == '':
                print('Pass')
                break

            if answer == value or answer in value:
                counter += 1
                print('Correct')
                break
            else:
                print('Wrong!')

    print(f'Congratz! You guessed {counter} out of {len(array)} questions!')
    return


quiz_dict(questions)

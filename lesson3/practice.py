"""
    * Task 1
Написать функцию, которая выбрасывает одно из трех исключений: ValueError,
TypeError или RuntimeError случайным образом. В месте вызова функции
обрабатывать все три исключения.
    *
"""
import random
from functools import reduce


def three_exceptions():
    try:
        rnd = random.randint(0, 2)
        if rnd == 0:
            raise ValueError
        if rnd == 1:
            raise TypeError
        if rnd == 2:
            raise RuntimeError
    except ValueError as e:
        print('Wrong Value', e)
    except TypeError as e:
        print('Wrong Type', e)
    except RuntimeError as e:
        print('Wrong Runtime', e)


# three_exceptions()


"""
    Task 2:
    Написать функцию, которая принимает на вход список, если в списке все
    объекты типа int - сортирует его. Иначе выбрасывает ValueError.
"""


def sort_int(array):
    temp = []
    for i in array:
        if isinstance(i, int):
            temp.append(i)
        else:
            raise ValueError
    return sorted(temp)


# print(sort_int([2, 3, 4, 5, 6, 9, 1]))
# print(sort_int(['s', 4, 'z', 4]))


"""
    Task 3:
    Написать функцию, которая принимает словарь, преобразует все ключи
    словаря в строки и возвращает новый словарь.
"""


def new_dict(array):
    temp = {}
    for key, value in array.items():
        temp[str(key)] = value
    return temp


# print(new_dict({1: 1, 2: 2, 3: 3}))


"""
    Task 4:
    Написать функцию, которая принимает список чисел и возвращает их
    произведение.
"""


my_list = [3, 2, 3, 10]
mult_all = reduce(lambda x, y: x * y, my_list)
print(mult_all)

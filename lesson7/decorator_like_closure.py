#


def logger(func):
    def inner(x, y):
        result = func(x, y)
        print('Result is', result)
        return result
    return inner


def sum(x, y):
    return x + y


l_sum = logger(sum)
print(l_sum(3, 3))

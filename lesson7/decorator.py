#


def logger(func):
    def inner(x, y):
        rst = func(x, y)
        print('Result is', rst)
        return rst
    return inner


@logger  # name of func
def sum(x, y):
    return x + y


print(sum(5, 6))

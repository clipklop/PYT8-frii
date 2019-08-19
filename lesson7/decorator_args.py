#


def action_decor(func):
    def inner(*args, **kwargs):
        rst = func(*args, **kwargs)
        print(f'Result is {rst}')
        return rst
    return inner


@action_decor
def x(x, y, z):
    return x * 2 + y - z


print(x(2, 3, 2))

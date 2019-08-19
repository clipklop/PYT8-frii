#


def fact_cache(func):
    cache = {}

    def inner(*args):
        x = args[0]
        if x in cache.keys():
            print(cache)
            return cache[x]
        else:
            result = func(*args)
            cache[x] = result
            return result
    return inner


@fact_cache
def factorial(x):
    if x == 0:
        return 1
    else:
        import time
        time.sleep(1)
        return x * factorial(x - 1)


c = factorial(4)
c = factorial(5)
c = factorial(6)
c = factorial(7)

print(c)

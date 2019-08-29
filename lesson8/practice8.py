import random


class mygen:
    def __init__(self, lst):
        self.__current = 0
        self.lst = lst

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current == len(self.lst):
            self.__current = 0
            raise StopIteration()

        result = self.lst[self.__current]
        self.__current += random.randint(0, result)
        return result


# c = mygen([3, 2, 5, 9])
# print(next(c), next(c), next(c))


class myrange:
    def __init__(self, to, from_=0, step=1):
        self.to = to
        self.from_ = from_
        self.step = step

        print(self.to, self.from_)

    def __iter__(self):
        return self

    def __next__(self):
        if self.from_ < self.to:
            i = self.from_
            self.from_ += self.step
            return i
        else:
            raise StopIteration()
            self.from_ = 0

    def __str__(self):
        return f'{myrange.__name__}({self.from_}, {self.to})'


# x = MyRange(5)
# print(x)


class mymap:
    def __init__(self, func, lst):
        self.__current = 0
        self.lst = lst
        self.func = func

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current == len(self.lst):
            self.__current = 0
            raise StopIteration()

        result = self.lst[self.__current]
        self.__current += self.func(self.__current)
        yield result


m = mymap(lambda x: x, [4,3,2,1])
print(m, next(m), next(m), next(m))

#


ten = lambda x: x * 10
print(ten(2))

l = lambda *args: print(*args)
l(list(range(1, 10)))

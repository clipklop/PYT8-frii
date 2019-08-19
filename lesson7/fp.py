#


from functools import reduce


# map
maps = list(range(1, 10, 2))

m = map(lambda x: x * 2, maps)
print(next(m), next(m), next(m), next(m), next(m))


# filter
f = filter(lambda x: x > 0, [-1, -5, -9, 20, 3, 9])
fm = list(map(lambda x: x * 3, f))
print(list(f))
print(fm)


# reduce
rlst = [1, 4, 2, 3]
result = reduce(lambda x, y: x + y, rlst)
print(result)

# pseudo mutable list
r = [1, 4, 2, 3, 5]
x = reduce(lambda x, y: x + [y], r, [])
print(x)

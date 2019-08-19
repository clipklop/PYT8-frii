lst_comp = [
    j for v in range(2, 5)
    for i in range(2, v)
    for j in range(i * 2, 10, i)
]

print(lst_comp)

for v in range(2, 5): # -> (2, 3, 4)
    for i in range(2, v): # -> (), (2), (2, 3) -> (4, 6)
        for j in range(i * 2, 10, i):
            print(j)

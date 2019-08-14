class Fun:
    def __init__(self, val):
        if isinstance(val, int):
            val = str(val)
        self.val = val

    def __add__(self, other):
        if isinstance(other, int):
            return Fun(self.val + str(other))
        elif isinstance(other, str):
            return Fun(self.val + other)
        elif isinstance(other, Fun):
            return Fun(self.val + str(other.val))
        else:
            raise TypeError("Unsupported type for addition")


x = Fun(5)
k = x
y = Fun(6)
z = x + y
print(z)
z = 7 + x
print(z)
z = z + "8"
print(z)
z = z + (1, 4)

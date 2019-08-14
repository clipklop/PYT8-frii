"""
    * A cart with bag design in basic OOP style
"""


class Cart():
    def __init__(self, volume):
        self.max_volume = volume
        self.volume = 0

    def add(self):
        self.volume += 1
        print(self.volume)

        if self.volume >= self.max_volume:
            print('Sorry no space left')


class Bag(Cart):
    pass


cart = Cart(4)
print(cart.volume)

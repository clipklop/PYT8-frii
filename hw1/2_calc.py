"""
    * A simple calc app
"""


def calc(nums=[], total=0):
    while True:
        inp = input("Введите число: ")

        if inp == '':
            print("Ok, I'm out")
            break

        if inp.isdigit():
            nums.append(int(inp))
            print(nums)

        if len(nums) == 2:
            inp = input("Введите действие (+, -, *, /): ")
            if inp == '+':
                total = nums[0] + nums[1]
                print(total)
                nums = []
            elif inp == '-':
                total = nums[0] - nums[1]
                print(total)
                nums = []
            elif inp == '*':
                total = nums[0] * nums[1]
                print(total)
                nums = []
            elif inp == '/':
                total = nums[0] / nums[1]
                print(total)
                nums = []

calc()

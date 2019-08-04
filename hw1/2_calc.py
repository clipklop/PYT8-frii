"""
    * A simple calc app
"""


def math_ops(op, num1, num2):
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2
    if op == '*':
        return num1 * num2
    if op == '/':
        return num1 // num2


def calc(total=0, num=0):
    inp = input("Введите действие или число: ")
    while True:
        if inp == '':
            print(f"Итоговый результат: {total}")
            break

        if inp in ['+', '-', '*', '/']:
            op = inp
            print(inp)

        if inp.isdigit():
            num = int(inp)
            if total == 0:
                total += num
                print(total)
            else:
                total = math_ops(op, total, num)
                print(f"Промежуточный итог: {total}")

        inp = input("Введите следующее действие или число: ")


calc()

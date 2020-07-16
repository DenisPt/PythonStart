def max_three1(x, y, z):
    li = [x, y, z]
    li.sort()
    return li[-1] + li[-2]


def max_three2(x, y, z):
    return max(x, y) + max(y, z) + max(x, z) - max(x, y, z)


try:
    x = float(input("x = "))
    y = float(input("y = "))
    z = float(input("z = "))
    print(f'Сумма двух максимальных = {max_three1(x, y, z)}')
    print(f'Сумма двух максимальных = {max_three2(x, y, z)}')

    """Минимальное решение"""
    print(f'Сумма двух максимальных = {(lambda x1, y1, z1: x1 + y1 + z1 - min(x1, y1, z1))(x, y, z)}')
except ValueError:
    print("Введены не числа!")
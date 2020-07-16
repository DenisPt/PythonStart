def power2(x2, y2):
    y2 = abs(y2)
    x4 = 1
    for i in range(y2):
        x4 *= 1/x2
    return x4


def power3(x3, y3):
    """Через рекурсию, знаю, что не проходили :)"""
    return 1 if y3 == 0 else 1 / x3 * power3(x3, y3 + 1)


x = input("x = ")
y = input("y = ")
try:
    x = float(x)
    y = int(y)
    if y < 0:
        """Первый способ"""
        print(f'{x} в степени {y} = {(lambda x1, y1: x1 ** y1)(x, y)}')

        """Второй способ"""
        print(f'{x} в степени {y} = {power2(x, y)}')

        """Третий способ"""
        print(f'{x} в степени {y} = {power3(x, y)}')
    else:
        print("'y' должен быть отрицательным")
except ValueError:
    print("'x' должен быть числом, а 'y' целым отрицательным числом")
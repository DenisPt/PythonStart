def divis1(x, y):
    return "Вы пытаетесь поделить на ноль!" if y == 0 else x/y


def divis2(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Попытка поделить на ноль!"


x = input("x = ")
y = input("y = ")
try:
    x, y = float(x), float(y)
    print(divis1(x, y))
    print(divis2(x, y))
except ValueError:
    print("Введены не числа!")
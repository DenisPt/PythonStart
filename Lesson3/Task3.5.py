def sum(args):
    global s, t
    for x in args:
        try:
            s += float(x)
        except ValueError:
            t = '@'
            break
    pass


s = 0
t = ''
while True:
    numbers = input("Введите несколько чисел через пробел или любой другой символ для завершения: ").split()
    sum(numbers)
    print(f"Сумма = {s}")
    if t == '@':
        break

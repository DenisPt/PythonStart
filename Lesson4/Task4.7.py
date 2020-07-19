def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)


def fact(n):
    for i in range(1, n + 1):
        yield fac(i)


x = int(input("Введите целое число x для вывода значений от 1! до x!: "))
for i in range(1, x + 1):
    print([el for el in fact(i)])

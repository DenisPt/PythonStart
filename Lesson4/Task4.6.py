from itertools import count, cycle

x = int(input("Введите целое число, с которого начнется генератор: "))
y = int(input("Введите целое число, на котором остановиться генератору: "))

# Первый вариант решения
def intg(x, ma):
    for i in count(x):
        if i <= ma:
            yield i
        else:
            break
for a in intg(x, y):
    print(a)

# Второй вариант решения без break
def intg2(x):
    yield x
for a in range(x, y + 1):
    print(next(intg2(a)))


list1 = input("Введите список слов через пробел: ").split()
m = int(input("Введите число повторений списка: "))
m *= len(list1)
list1 = cycle(list1)
for i in range(m):
    print(next(list1))

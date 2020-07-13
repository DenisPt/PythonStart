rate = [7, 5, 3, 3, 2]
while True:
    n = int(input("Введите число: "))
    rate.reverse()
    for i in range(len(rate)):
        if rate[i] >= n:
            rate.insert(i, str(n))
            break
    rate.reverse()
    print(rate)
    break
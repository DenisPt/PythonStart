List1 = ["зима", "весна", "лето", "осень"]
Dict1 = {0 : "зима", 1: "весна", 2: "лето", 3: "осень"}
while True:
    n = input("Введите № месяца: ")
    if n.isdigit():
        if int(n) > 0 and int(n) < 13:
            n = int(n)
            n = (n // 3) % 4
            print(f"Это {List1[n]}!")
            print(f"Это {Dict1.get(n)}!!")
            break
        else:
            print("Вы ввели неверное значение месяца")
    else:
        print("Вы ввели неверное значение месяца")

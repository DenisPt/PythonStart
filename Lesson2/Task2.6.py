Goods = []

while True:
    name = input("Введите название товара: ")
    price = int(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    unit = input("Введите ед.измерения: ")
    Goods.append((len(Goods) + 1, {"название": name, "цена": price, "количество": quantity, "eд. изм.": unit}))
    yn = input("Хотите продолжить? (да/нет): ")
    while yn != "да" and yn != "нет":
        print("Попробуйте еще раз")
        yn = input("Хотите продолжить? (да/нет): ")
    if yn == "нет":
        break

name = []
price = []
quantity = []
unit = []

for g in range(len(Goods)):
    name.append(Goods[g][1].get("название"))
    price.append(Goods[g][1].get("цена"))
    quantity.append(Goods[g][1].get("количество"))
    unit.append(Goods[g][1].get("ед. изм."))

Analyt = {"название": name, "цена": price, "количество": quantity, "ед. изм.": unit}

print(Analyt)

Goods = []
nGoods = 0
while True:
    yn = input("Хотите продолжить? (да/нет): ")
    if yn == "нет":
        break
    elif yn == "да":
        nGoods += 1
        name = input("Введите название товара: ")
        price = int(input("Введите цену товара: "))
        quantity = int(input("Введите количество товара: "))
        unit = input("Введите ед.измерения: ")
        Goods.append((nGoods, {"название": name, "цена": price, "количество": quantity, "eд": unit}))
    else:
        print("Попробуйте еще раз")
#for g in Goods:


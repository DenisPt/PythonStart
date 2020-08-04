from abc import ABC, abstractmethod
from os import system


class MyErr(Exception):
    def __init__(self, txt):
        self.txt = txt


class Object(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name
        self.inv = {}  # доступное оборудование

    @abstractmethod
    def accept(self, device):
        pass

    def __str__(self):
        m = f"Объект '{self.name}':\n"
        for dev, inv in self.inv.items():
            m += f"{str(OfficeEquip.devices.get(dev))} - {inv} шт.\n"
        return m


class Stock(Object):
    def __init__(self, name):
        super().__init__(name)

    def accept(self, device, obj="producer", quantity=1):
        try:
            quantity = int(quantity)
            if quantity < 0:
                raise MyErr("")
            if obj == "producer":
                self.inv.update(
                    {device.code: quantity if self.inv.get(device.code) == None else self.inv.get(
                        device.code) + quantity})
            else:
                if obj.inv.get(device.code) != None:
                    if obj.inv.get(device.code) <= quantity:
                        q = obj.inv.pop(device.code)
                    else:
                        obj.inv.update({device.code: obj.inv.get(device.code) - quantity})
                        q = quantity
                    self.inv.update(
                        {device.code: q if self.inv.get(device.code) == None else self.inv.get(device.code) + q})
                    print(
                        f"Перемещено {q} шт. товара {str(OfficeEquip.devices.get(device.code))} с '{obj.name}' на '{self.name}'")
                else:
                    print(f"Невозможно переместить {str(device)}, т.к. на {obj.name} он отсутствует")
        except (MyErr, ValueError):
            print("Введите целое, положительное количество для перемещения!")


class SubDiv(Object):
    def __init__(self, name):
        super().__init__(name)

    def accept(self, device, obj, quantity=1):
        try:
            quantity = int(quantity)
            if quantity < 0:
                raise MyErr("")
            if obj.inv.get(device.code) != None:
                if obj.inv.get(device.code) <= quantity:
                    q = obj.inv.pop(device.code)
                else:
                    obj.inv.update({device.code: obj.inv.get(device.code) - quantity})
                    q = quantity
                self.inv.update(
                    {device.code: q if self.inv.get(device.code) == None else self.inv.get(device.code) + q})
                print(
                    f"Перемещено {q} шт. товара {str(OfficeEquip.devices.get(device.code))} с '{obj.name}' на '{self.name}'")
            else:
                print(f"Невозможно переместить {str(device)}, т.к. на {obj.name} он отсутствует")
        except (MyErr, ValueError):
            print("Введите целое, положительное количество для перемещения!")


class OfficeEquip(ABC):
    code = 0
    devices = {}

    @abstractmethod
    def __init__(self, producer, model, isprint, isscan, form):
        self.code = OfficeEquip.code + 1  # внутренний код
        OfficeEquip.code += 1
        self.producer = producer  # производитель
        self.model = model  # модель
        self.isprint = isprint  # имеется ли функция печати (True/False)
        self.isscan = isscan  # имеется ли функция сканера (True/False)
        self.form = form  # Форм-фактор
        OfficeEquip.devices.update({self.code: self})

    def __str__(self):
        return f"{self.code:04d} - {self.producer} - {self.model}"

    @abstractmethod
    def getchars(self):
        print(f"Характеристики устройства {str(self)}:")
        print("Умеет печатать" if self.isprint else "Не умеет печатать")
        print("Умеет сканировать" if self.isscan else "Не умеет сканировать")
        print(f"Максимальный формат бумаги: {self.form}")


class Printer(OfficeEquip):
    def __init__(self, producer, model, iscolor, form, islaser):
        super().__init__(producer, model, True, False, form)
        self.iscolor = iscolor  # цветная печать (True/False)
        self.islaser = islaser  # лазерный (True/False)

    def getchars(self):
        super().getchars()
        print("Цветная печать" if self.iscolor else "Ч/б печать")
        print("Лазерный" if self.islaser else "Струйный")
        print()


class Scanner(OfficeEquip):
    def __init__(self, producer, model, form):
        super().__init__(producer, model, False, True, form)

    def getchars(self):
        super().getchars()
        print()


class MulDevice(OfficeEquip):
    def __init__(self, producer, model, iscolor, form, islaser):
        super().__init__(producer, model, True, True, form)
        self.iscolor = iscolor  # цветная печать (True/False)
        self.islaser = islaser  # лазерный (True/False)

    def getchars(self):
        super().getchars()
        print("Цветная печать" if self.iscolor else "Ч/б печать")
        print("Лазерный" if self.islaser else "Струйный")
        print()


def add_device():
    while True:
        try:
            typ = input("Выберете тип устройства, которое хотите добавить в систему:"
                        "\n1 - Принтер\n2 - Сканнер\n3 - МФУ\nили введите 'stop' для завершения добавления устройства ")
            if typ == "stop":
                return None
            typ = int(typ)
            if not 1 <= typ <= 3:
                raise MyErr("Введите число 1, 2 или 3")
        except (MyErr, ValueError) as err:
            print(err)
        else:
            break
    producer = input("Введите производителя: ")
    model = input("Введите модель: ")
    try:
        for dev in OfficeEquip.devices.values():
            if dev.producer == producer and dev.model == model:
                raise MyErr("Устройство уже существует")
    except MyErr as err:
        print(err)
        return None
    form = input("Введите максимальный формат бумаги для использования: ")
    if typ == 1 or typ == 3:
        while True:
            try:
                iscolor = input("Устройство цветное (Да/Нет): ")
                if iscolor != "Да" and iscolor != "Нет":
                    raise MyErr("Введите 'Да' или 'Нет'")
            except MyErr as err:
                print(err)
            else:
                iscolor = True if iscolor == "Да" else False
                break
        while True:
            try:
                islaser = input("Устройство лазерное (Да/Нет): ")
                if islaser != "Да" and islaser != "Нет":
                    raise MyErr("Введите 'Да' или 'Нет'")
            except MyErr as err:
                print(err)
            else:
                islaser = True if islaser == "Да" else False
                break
    if typ == 1:
        return Printer(producer, model, iscolor, form, islaser)
    elif typ == 2:
        return Scanner(producer, model, form)
    elif typ == 3:
        return MulDevice(producer, model, iscolor, form, islaser)


stocks = []
subdivs = []
devices = []
stocks.append(Stock("Склад1"))
subdivs.append(SubDiv("Подразделение1"))
subdivs.append(SubDiv("Подразделение2"))

devices.append(MulDevice("Xerox", "MP230", False, "A4", True))
devices.append(Printer("Xerox", "M230", False, "A4", True))

stocks[0].accept(devices[0], "producer", 30)
stocks[0].accept(devices[1], "producer", 100)
subdivs[0].accept(devices[0], stocks[0], 3)
subdivs[0].accept(devices[1], stocks[0], 10)
subdivs[1].accept(devices[0], stocks[0], 5)
subdivs[1].accept(devices[1], stocks[0], 15)

while True:
    stop = input("Добавим несколько устройств в систему, для окончания введите 'stop', иначе нажмите Enter: ")
    if stop == "stop":
        break
    else:
        devices.append(add_device())
print([str(dev) for dev in devices])
while True:
    try:
        print("Вам доступны следующие действия: ")
        print("1 - Добавить новый склад")
        print("2 - Добавить новое подразделение")
        print("3 - Добавить новое устройство")
        print("4 - Посмотреть остатки на объекте")
        print("5 - Заказать устройства от производителя на один из складов")
        print("6 - Переместить устройства между объектами")
        print("7 - Посмотреть список устройств в системе")
        print("8 - Посмотреть характеристики устройства")
        print("9 - Завершить программу")
        act = int(input("Выберите один из вариантов: "))
        if not 1 <= act <= 9:
            raise MyErr("")
        if act == 1:
            try:
                name = input("Введите имя нового склада или 'stop' для отмены: ")
                if name == 'stop':
                    pass
                for st in stocks:
                    if name == st.name:
                        raise MyErr("Такое имя уже присутствует!")
            except MyErr as err:
                print(err)
            else:
                stocks.append(Stock(name))
        elif act == 2:
            try:
                name = input("Введите имя нового подразделения или 'stop' для отмены: ")
                if name == 'stop':
                    pass
                for sd in subdivs:
                    if name == sd.name:
                        raise MyErr("Такое имя уже присутствует!")
            except MyErr as err:
                print(err)
            else:
                stocks.append(Stock(name))
        elif act == 3:
            dev = add_device()
            if dev != None:
                devices.append(dev)
        elif act == 4:
            try:
                st = input(
                    "Введите 0 для просмотра остатков на складе, 1 для просмотра остатков на подразделении или 'stop' для отмены: ")
                if st == "stop":
                    pass
                if st != "0" and st != "1":
                    raise MyErr("Введите 0 или 1")
            except MyErr as err:
                print(err)
            else:
                try:
                    if int(st):
                        print("Выберите подразделение: ")
                        for i, sd in enumerate(subdivs):
                            print(f"{i + 1} - {sd.name}")
                        st = int(input(": "))
                        if not st - 1 in range(len(subdivs)):
                            raise MyErr("Вы ввели неверный диапазон!")
                        print(subdivs[st - 1])
                    else:
                        print("Выберите склад: ")
                        for i, st in enumerate(stocks):
                            print(f"{i + 1} - {st.name}")
                        sd = int(input(": "))
                        if not sd - 1 in range(len(stocks)):
                            raise MyErr("Вы ввели неверный диапазон!")
                        print(stocks[sd - 1])
                except (MyErr, ValueError) as err:
                    print(err)
        elif act == 5:
            try:
                print("Выберите склад: ")
                for i, st in enumerate(stocks):
                    print(f"{i + 1} - {st.name}")
                st = int(input(": "))
                if not st - 1 in range(len(stocks)):
                    raise MyErr("Вы ввели неверный диапазон!")
                print("Выберите устройство: ")
                for i, dev in enumerate(devices):
                    print(f"{i + 1} - {str(dev)}")
                dev = int(input(": "))
                if not dev - 1 in range(len(devices)):
                    raise MyErr("Вы ввели неверный диапазон!")
                q = int(input("Введите количество к заказу: "))
                stocks[st - 1].accept(devices[dev - 1], "producer", q)
            except (MyErr, ValueError) as err:
                print(err)
        elif act == 6:
            try:
                print("Выберите отправителя:")
                out = input(
                    "Введите 0 для выбора склада, 1 для выбора подразделения: ")
                if out != "0" and out != "1":
                    raise MyErr("Введите 0 или 1")
            except MyErr as err:
                print(err)
            else:
                try:
                    if int(out):
                        print("Выберите подразделение: ")
                        for i, sd in enumerate(subdivs):
                            print(f"{i + 1} - {sd.name}")
                        st1 = int(input(": "))
                        if not st1 - 1 in range(len(subdivs)):
                            raise MyErr("Вы ввели неверный диапазон!")
                        out = subdivs[st - 1]
                    else:
                        print("Выберите склад: ")
                        for i, sd in enumerate(stocks):
                            print(f"{i + 1} - {sd.name}")
                        st1 = int(input(": "))
                        if not st1 - 1 in range(len(stocks)):
                            raise MyErr("Вы ввели неверный диапазон!")
                        out = stocks[st1 - 1]
                except (MyErr, ValueError) as err:
                    print(err)
            try:
                print("Выберите получателя:")
                inp = input(
                    "Введите 0 для выбора склада, 1 для выбора подразделения: ")
                if inp != "0" and inp != "1":
                    raise MyErr("Введите 0 или 1")
            except MyErr as err:
                print(err)
            else:
                try:
                    if int(inp):
                        print("Выберите подразделение: ")
                        for i, sd in enumerate(subdivs):
                            print(f"{i + 1} - {sd.name}")
                        st2 = int(input(": "))
                        if not st2 - 1 in range(len(subdivs)):
                            raise MyErr("Вы ввели неверный диапазон!")
                        inp = subdivs[st2 - 1]
                    else:
                        print("Выберите склад: ")
                        for i, sd in enumerate(stocks):
                            print(f"{i + 1} - {sd.name}")
                        st2 = int(input(": "))
                        if not st2 - 1 in range(len(stocks)):
                            raise MyErr("Вы ввели неверный диапазон!")
                        inp = stocks[st2 - 1]
                except (MyErr, ValueError) as err:
                    print(err)
            try:
                print("Выберите устройство: ")
                for i, dev in enumerate(devices):
                    print(f"{i + 1} - {str(dev)}")
                dev = int(input(": "))
                if not dev - 1 in range(len(devices)):
                    raise MyErr("Вы ввели неверный диапазон!")
                dev = devices[dev - 1]
                q = int(input("Введите количество к перемещению: "))
                inp.accept(dev, out, q)
            except (MyErr, ValueError) as err:
                print(err)
        elif act == 7:
            print([str(dev) for dev in devices])
        elif act == 8:
            print("Выберите устройство: ")
            for i, dev in enumerate(devices):
                print(f"{i + 1} - {str(dev)}")
            dev = int(input(": "))
            if not dev - 1 in range(len(devices)):
                raise MyErr("Вы ввели неверный диапазон!")
            devices[dev - 1].getchars()
        elif act == 9:
            break
        input("Нажмите Enter для продолжения")
    except (MyErr, ValueError):
        print("Введите число от 1 до 9")

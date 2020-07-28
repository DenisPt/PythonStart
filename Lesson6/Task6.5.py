class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title="ручка"):
        super().__init__(title)
        self.title2 = "ручкой"

    def draw(self):
        print("-------------------")


class Pencil(Stationery):
    def __init__(self, title="карандаш"):
        super().__init__(title)
        self.title2 = "карандашом"

    def draw(self):
        print("...................")


class Handle(Stationery):
    def __init__(self, title="маркер"):
        super().__init__(title)
        self.title2 = "маркером"

    def draw(self):
        print("###################")


stat = ("ручка", "карандаш", "маркер")

while True:
    print("Доступные предметы:")
    for s in stat:
        print(s + ",", end="\t")
    typ = input("\nВыберите один из предметов выше: ")
    if typ not in stat:
        print("Попробуйте еще раз!")
    elif typ == "ручка":
        st = Pen()
        break
    elif typ == "карандаш":
        st = Pencil()
        break
    else:
        st = Handle()
        break

print(f"Порисуем {st.title2}: ")
st.draw()

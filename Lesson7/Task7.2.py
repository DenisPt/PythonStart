from abc import ABC, abstractmethod


class Garment(ABC):
    @abstractmethod
    def footage(self):
        pass


class Coat(Garment):
    def __init__(self, v):
        self.v = v

    @property
    def footage(self):
        return self.v / 6.5 + 0.5


class Blazer(Garment):
    def __init__(self, h):
        self.h = h

    @property
    def footage(self):
        return self.h * 2 + 0.3

while True:
    try:
        c_1 = Coat(int(input("Введите размер плаща для пошива: ")))
        break
    except ValueError:
        print("Попробуйте еще раз, введите целое число!")
while True:
    try:
        b_1 = Blazer(int(input("Введите Ваш рост в см для пошива пиджака: ")))
        break
    except ValueError:
        print("Попробуйте еще раз, введите целое число!")
print(f"Для пошива плаща Вам необходимо закупить {c_1.footage / 100:.2f}м ткани")
print(f"Для пошива пиджака Вам необходимо закупить {b_1.footage / 100:.2f}м ткани")

from math import sqrt


class Iterator_O_strings:
    def __init__(self, w=0, d=1):
        self.w = w
        self.d = d

    def __next__(self):
        x = min(self.w, self.d)
        if 0 < self.w <= self.d:
            self.w = 0
            return "o " * x
        elif self.w > self.d:
            self.w -= self.d
            return "o " * self.d
        else:
            raise StopIteration


class O_strings:
    def __init__(self, w, d):
        self.w = w
        self.d = d

    def __iter__(self):
        return Iterator_O_strings(self.w, self.d)


class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > other.cells:
            return Cell(self.cells - other.cells)
        else:
            print("Нельзя из маленькой клетки вычесть большую")
            return ValueError

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, d):
        for cells in O_strings(self.cells, d):
            print(cells)

    # через print будет выводиться клетка,  наиболее близкая к квадрату
    def __str__(self):
        st = ""
        for cel in O_strings(self.cells, round(sqrt(self.cells))):
            st += cel + "\n"

        return "--" * round(sqrt(self.cells)) +"\n" + st + "--" * round(sqrt(self.cells))


c_1 = Cell(20)
c_1.make_order(6)
print("---------------------")
c_2 = Cell(4)
print("с_1:\n" + str(c_1))
print("с_2:\n" + str(c_2))
print("c_1 * c_2:\n" + str(c_1 * c_2))
print("c_1 - c_2:\n" + str(c_1 - c_2))
print("c_1 + c_2:\n" + str(c_1 + c_2))
print("c_1 / c_2:\n" + str(c_1 / c_2))

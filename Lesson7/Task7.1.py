class Matrix:
    def __init__(self, matrix):
        self.h = len(matrix)  # высота матрицы
        self.w = 0  # длина матрицы, если строки разной длины - будет максимальная длина строки
        for st in matrix:
            self.w = max(self.w, len(st))

        for st in matrix:  # все строки добиваем до длины матрицы, недостающие элементы заполняем нулями
            if len(st) < self.w:
                st.extend([0 for _ in range(self.w - len(st))])
        self.matrix = matrix

    def __str__(self):
# нормально отображаются матрицы с 7-значными числами, если нужны числа длинее, в строке 19 поменять значение 8 на большее
        m = "-" * (self.w * 10 + 2) + "\n"
        for st in self.matrix:
            m += "|"
            for el in st:
                m += f"{el:8d} |"
            m += "\n"
        m += "-" * (self.w * 10 + 2)
        return m

    def __add__(self, other):
        if self.w == other.w and self.h == other.h:
            return Matrix([[self.matrix[j][i] + other.matrix[j][i] for i in range(self.w)] for j in range(self.h)])
        else:
            print("-" * self.w * 10 + "\n" + "-" * self.w * 10)
            print("Размеры матриц не совпадают!")
            return Matrix([[]])


m_1 = Matrix([[1], [1, 111111], [1, 111, 1], [111, 11111]])
m_2 = Matrix([[2], [2, 222222], [2, 222, 2], [222, 22222]])
print(m_1)
print(" " * (m_1.w * 5) + "+")
print(m_2)
print(" " * (m_2.w * 5) + "||")
print(m_1 + m_2)

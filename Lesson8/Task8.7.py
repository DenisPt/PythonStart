class Complex():
    imunit = "i"

    def __init__(self, real, imag):
        self.real = float(real)
        self.imag = float(imag)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __truediv__(self, other):
        return Complex((self.real * other.real + self.imag * other.imag) / (other.real ** 2 - other.imag ** 2),
                       (self.imag * other.real - self.real + other.imag) / (other.real ** 2 - other.imag ** 2))

    def __str__(self):
        if not self.imag:
            im = ""
        elif self.imag > 0:
            im = f"+{str(self.imag) + Complex.imunit}"
        else:
            im = f"{str(self.imag) + Complex.imunit}"
        return f"{str(self.real) + im}"

    @classmethod
    def chageim(cls, im):
        Complex.imunit = im

    @classmethod
    def get_im_num(cls):
        while True:
            try:
                real, imag = input("Введите действительную и мнимую часть через пробел: ").split(" ")
                return Complex(float(real), float(imag))
            except ValueError:
                print("Вы ввели неверный формат чисел!")


print("Задайте комплексное число x")
x = Complex.get_im_num()
print("Задайте комплексное число y")
y = Complex.get_im_num()
print(f"x = {x}")
print(f"y = {y}")
print(f"x + y = {x + y}")
print(f"x - y = {x - y}")
print(f"x * y = {x * y}")
print(f"x / y = {x / y}")

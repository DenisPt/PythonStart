class Road:
    def __init__(self, leng, wid):
        self._length = float(leng)
        self._width = float(wid)
    def mass(self, mass1sm, thick):
        return self._length * self._width * mass1sm * thick
try:
    r = Road(input("Введите длину дороги (в м): "), input("Введите ширину дороги (в м): "))
    try:
        print("Необходимая масса для покрытия = " +
              f"{r.mass(float(input('Введите массу на 1 см асфальта (в кг): ')), float(input('Введите толщину дороги (в см): ')))/1000:.0f} т")
    except ValueError:
        print("Масса и толщина должны быть числами!")
except ValueError:
    print("Длина и ширина должны быть числами!")

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.__position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname
    def get_total_income(self):
        print(f"Полный доход работника составляет {sum(self._income.values())}")

name = input("Введите имя работника: ")
sname = input("Введите фамилию работника: ")
pos = input("Введите должность работника: ")
wage = input("Введите оклад работника: ")
bonus = input("Введите премию работника: ")
try:
    worker = Position(name, sname, pos, wage, bonus)
    print(f"Работника зовут: {worker.get_full_name()}, а работает он на должности {worker._Worker__position}")
    worker.get_total_income()
except ValueError:
    print("Оклад и премия должны быть целыми числами!")

from time import sleep


class Car:
    # справочник направлений
    directions = ("Прямо", "Налево", "Направо", "Назад")

    def __init__(self, maxspeed, color, name, is_police=False):
        self.maxspeed = maxspeed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed = 0
        self.direction = "Прямо"

    def go(self):
        if not self.speed:
            print(f"Ваш автомобиль '{self.name}' тронулся!")
            self.speed = 1
        else:
            print("Вы уже в пути!")

    def stop(self):
        if not self.speed:
            print("Вы и так стоите!")
        else:
            if self.speed <= 20:
                print("Остановились!")
                self.speed = 0
            else:
                print("Вы не можете так резко остановиться, снизьте скорость до 20!")

    def accelerate(self, speed, maxacc=10):
        if not self.speed:
            self.go()
        if speed > maxacc:
            print(f"Вы пытаетесь слишком быстро разогнаться! Машина ускорена не более чем на {maxacc}")
            speed = maxacc
        if self.speed + speed > self.maxspeed:
            print(f"Вы не можете ехать быстрее чем {self.maxspeed}, скорость ограничена")
            self.speed = self.maxspeed
        else:
            self.speed += speed
        self.show_speed()

    def decelerate(self, speed, maxdec=20):
        if speed > maxdec:
            print(f"Вы пытаетесь слишком быстро замедлиться! Машина замедлена не более чем на {maxdec}")
            speed = maxdec
        if self.speed < speed:
            self.stop()
        else:
            self.speed -= speed
        self.show_speed()

    def turn(self, direct):
        if direct in Car.directions:
            print(f"Едем {direct}!")
            self.direction = direct
        else:
            print(f"Неверное направление, продолжаем ехать {self.direction}")

    def beep(self):
        print("Beep! Beep!")

    def show_speed(self):
        print(f"Ваша скорость {self.speed}")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Слишком высокая скорость!")


class SportCar(Car):
    def __init__(self, maxspeed, color, name):
        Car.__init__(self, maxspeed, color, name)

    def accelerate(self, speed, maxacc=30):
        Car.accelerate(self, speed, maxacc)


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Слишком высокая скорость!")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, True)

    def beep(self):
        for _ in range(3):
            print("oouuiiwioouiuiwiii")
            sleep(1)

while True:
    start = input("Введите любой символ если хотите провести тест-драйв или 'q' для выхода: ")
    if start == 'q':
        break
    typesofcar = {1: "Городской", 2: "Спортивный", 3: "Рабочий", 4: "Полицейский"}
    print("Типы автомобилей, которые Вы можете использовать: ")
    for t in typesofcar:
        print(f"{t} - {typesofcar.get(t)}")

    while True:
        try:
            type = int(input("Введите цифру для выбора типа автомобиля, который Вы хотите использовать: "))
            if type - 1 not in range(4):
                print("Введите цифру от 1 до 4!")
            else:
                break
        except ValueError:
            print("Введите цифру от 1 до 4!")
    print(f"Отлично, Вы выбрали {typesofcar.get(type)} автомобиль")

    while True:
        try:
            maxspeed = int(input("Введите максимальную скорость для Вашего авто: "))
            if maxspeed < 60 and type == 2:
                print("Скорость для спортивного авто должна быть не меньше 60!")
            else:
                break
        except ValueError:
            print("Введите целое число!")
    color = input("Введите цвет Вашего авто: ")
    name = input("И давайте назовем Ваш авто: ")

    if type == 1:
        car = TownCar(maxspeed, color, name)
    elif type == 2:
        car = SportCar(maxspeed, color, name)
    elif type == 3:
        car = WorkCar(maxspeed, color, name)
    else:
        car = PoliceCar(maxspeed, color, name)

    commands = {1: "Стартануть", 2: "Остановиться", 3: "Ускориться",
                4: "Замедлиться", 5: "Повернуть", 6: "Посигналить",
                7: "Показать скорость", 8: "Закончить тест-драйв"}

    while True:
        try:
            print("Вам доступны следующие команды: ")
            for c in commands:
                print(f"{c} - {commands.get(c)}", end="\t")
            command = int(input("\nВыберите команду: "))
            if command == 8:
                break
            elif command == 1:
                car.go()
            elif command == 2:
                car.stop()
            elif command == 3:
                while True:
                    try:
                        a = int(input("Введите ускорение, которое хотите добавить к скорости: "))
                        break
                    except ValueError:
                        print("Введите целое число!")
                car.accelerate(a)
            elif command == 4:
                while True:
                    try:
                        a = int(input("Введите замедление, которое хотите отнять от скорости: "))
                        break
                    except ValueError:
                        print("Введите целое число!")
                car.decelerate(a)
            elif command == 5:
                while True:
                    print("Возможные направления движения: ")
                    for d in Car.directions:
                        print(d, end="\t")
                    d = input("\nВыберите направление: ")
                    if d in Car.directions:
                        car.turn(d)
                        break
                    print("Вы выбрали неверное направление, попробуйте еще раз!")
            elif command == 6:
                car.beep()
            elif command == 7:
                car.show_speed()
            else:
                print("Введите число от 1 до 8!")
        except ValueError:
            print("Введите число от 1 до 8!")

print("Спасибо,что выбрали наш автосалон!")
for _ in range(3):
    print(3 - _)
    sleep(1)
print("Пока!")
sleep(1)

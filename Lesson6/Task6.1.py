from time import sleep


class TrafficLight:

    lightstime = {"красный": 7, "зеленый": 15, "желтый": 2}

    def __init__(self, color):
        if color in TrafficLight.lightstime.keys():
            self.__color = color
            if color == "красный":
                self.prevcolor = "зеленый"
            else:
                self.prevcolor = "красный"
        else:
            print("Вы ввели неверный цвет!")

    def running(self, timerunning):
        for i in range(timerunning):
            for s in range(TrafficLight.lightstime.get(self.__color)):
                print(f"Ждем {s+1} секунд{'' if s > 3 else 'у' if s == 0 else 'ы'}. Цвет светофора - {self.__color}")
                sleep(1)
            if self.__color != "желтый":
                self.prevcolor = self.__color
                self.__color = "желтый"
            elif self.prevcolor == "красный":
                self.__color = "зеленый"
            else:
                self.__color = "красный"
            print(f"Переключаемся на {self.__color}")


a = TrafficLight(input("Введите первый цвет светофора (красный/желтый/зеленый): "))
try:
    a.running(int(input("Введите сколько раз хотите переключить светофор: ")))
except:
    print("=(")

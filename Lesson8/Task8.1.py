class DateErr(Exception):
    def __init__(self, txt):
        self.txt = txt

class Date:
    d_in_month = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}"

    @classmethod
    def getdata(cls, date):
        day, month, year = date.split("-")
        return cls(day, month, year)

    @staticmethod
    def validdate(date):
        m = ""
        try:
            map(int, str(date).split("/"))
            # проверяем год
            try:
                if int(date.year) <= 1900:
                    raise DateErr("Люди столько не живут!")
                elif int(date.year) >= 2002:
                    raise DateErr("Вам должно быть больше 18!")
            except DateErr as err:
                m += str(err) + "\n"
            # проверяем месяц
            try:
                if int(date.month) < 1 or int(date.month) > 12:
                    raise DateErr("В году всего 12 месяцев!")
            except DateErr as err:
                m += str(err) + "\n"
            #проверяем дату
            try:
                if int(date.day) < 1 or int(date.day) > Date.d_in_month.get(int(date.month)):
                    raise DateErr("В этом месяце нет столько дней")
                elif int(date.year) % 4 != 0 and int(date.month) == 2 and int(date.day) == 29:
                    raise DateErr("Это не високосный год, в феврале 28 дней!")
            except DateErr as err:
                m += str(err)
        except ValueError:
            m += "День, месяц и год должны быть целыми числами!"
        return m if m != "" else "Все ок!"


while True:
    try:
        d = input("Введите дату рождения: ")
        if d.count("-") != 2:
            raise DateErr("Дата должна быть введена в формате dd-mm-yyyy!")
    except DateErr as err:
        print(err)
        print("Попробуйте еще раз!")
    else:
        d = Date.getdata(d)
        break
print("Проверим Вашу дату рождения:")
print(Date.validdate(d))
print(f"День вашего рождения - {d.day}")
print(f"Месяц вашего рождения - {d.month}")
print(f"Год вашего рождения - {d.year}")

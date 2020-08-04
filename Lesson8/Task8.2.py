class MyErr(Exception):
    def __init__(self, txt):
        self.txt = txt

x = input("Введите число, которое хотите поделить на ноль: ")
y = 0
try:
    if x == "Я - Чак Норрис!":
        raise MyErr("Вы выиграли!")
    elif not y:
        raise MyErr("Только Чак Норрис может делить на ноль!\nХорошая попытка!")
except MyErr as err:
    print(err)

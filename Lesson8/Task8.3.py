class ErrType(Exception):
    def __init__(self, txt):
        self.txt = txt

def add(args):
    global t, s
    for x in args:
        try:
            if x == "@":
                s = "@"
                break
            elif not x.isdigit():
                raise ErrType(f"Вводите только целые числа, или '@' для завершения, {x} - не целое")
        except ErrType as err:
            print(err)
        else:
            t.append(int(x))
    pass

s = ""
t = []
while True:
    numbers = input("Введите несколько целых чисел через пробел или '@' для завершения: ").split()
    add(numbers)
    if s == '@':
        break
print(f"Список: {t}")
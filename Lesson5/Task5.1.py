file_ = open("Task5.1.txt", "w", encoding="utf-8")
while True:
    inp = input("Введите строку или пустую строку для завершения: ")
    if inp == "":
        break
    print(inp, file=file_)
file_.close()

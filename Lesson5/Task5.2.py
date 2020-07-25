# Заккоментировать блок ниже, если есть созданный файл Task5.2.txt
import random
with open("Task5.2.txt", "w", encoding="utf-8") as file1:
    strings = range(random.randint(1, 30))
    for _ in strings:
        words = random.randint(1, 5)
        for __ in range(words):
            print(str(random.randint(1, 20000)), end=" ", file=file1)
        print(random.randint(1, 20000), file=file1)
# Окончание комментариев

# Рабочий код
try:
    with open("Task5.2.txt", "r", encoding="utf-8") as file1:
        content = [st.split() for st in file1.readlines()]
        print(f"Количество строк в файле: {len(content)}")
        for st in range(len(content)):
            print(f"Количество слов в строке {st + 1} = {len(content[st])}")
except IOError:
    print("Нет созданного файла Task5.2.txt")
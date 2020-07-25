# Заккоментировать блок ниже, если есть созданный файл Task5.3.txt
import random
with open("Task5.3.txt", "w", encoding="utf-8") as file1:
    print(f"Иванов {round(random.random()*20000+10000, 2)}", file=file1)
    print(f"Петров {round(random.random()*20000+10000, 2)}", file=file1)
    print(f"Сидоров {round(random.random()*20000+10000, 2)}", file=file1)
    print(f"Смирнов {round(random.random()*20000+10000, 2)}", file=file1)
    print(f"Иванец {round(random.random()*20000+10000, 2)}", file=file1)
    print(f"Иванченко {round(random.random()*20000+10000, 2)}", file=file1)
    print(f"Иванович {round(random.random()*20000+10000, 2)}", file=file1)
    print(f"Ивановиченко {round(random.random()*20000+10000, 2)}", file=file1)
    print(f"Смирнович {round(random.random()*20000+10000, 2)}", file=file1)
    print(f"Смирновченко {round(random.random()*20000+10000, 2)}", file=file1)
    print(f"Смирновенко {round(random.random()*20000+10000, 2)}", file=file1)
# Окончание комментариев

try:
    with open("Task5.3.txt", "r", encoding="utf-8") as file1:
        content = [st.split() for st in file1.readlines()]
        for string in content:
            string[1] = float(string[1])
        dic = {}
        for string in content:
            dic.update([string])
        smallsalary = []
        for family in dic.keys():
            if dic.get(family) < 20000:
                smallsalary.append(family)
        print("Сотрудники с маленькой зарплатой:", end="")
        for family in smallsalary:
            print(" " + family, end="")
        print()
        print(f"Средняя зарплата = {sum(dic.values())/len(dic):.0f}")
        print(dic)
except ValueError:
    print("Для зарплаты введены не целые значения, попробуйте снова")
except IOError:
    print("Нет созданного файла Task5.3.txt")
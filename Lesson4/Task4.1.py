from sys import argv

try:
    production = int(argv[1])
    salary = int(argv[2])
    prize = int(argv[3])
    print(f"Зарплата равна {(production * salary) + prize}")
except ValueError:
    print("Введены не числа!")
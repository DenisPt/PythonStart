import random
with open("Task5.5.txt", "w", encoding="utf-8") as file1:
    numbers = range(random.randint(1, 30))
    for _ in numbers:
        print(str(random.randint(1, 20000)), end=" ", file=file1)
    print(random.randint(1, 20000), file=file1)

with open("Task5.5.txt", "r", encoding="utf-8") as file1:
    print(sum(map(int, file1.readline().split())))
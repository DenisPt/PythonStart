str = input("Введите несколько слов через пробел: ")
str = str.split()
for word in str:
    print(word[:10])
print(str)
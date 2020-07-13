x=[]
while True:
    n = input("Введите новый элемент или 'Break' для завершения: ")
    if n.capitalize() == "Break":
        break
    else:
        x.append(n)
i=0
for i in range(len(x) // 2):
    if len(x) == 1:
        break
    x[2*i], x[2*i+1] = x[2*i+1], x[2*i]
print(x)
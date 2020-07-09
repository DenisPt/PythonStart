# Task6
x = float(input('Input positive number: '))
y = float(input("Input other positive number: "))
i = 1
while x < y:
    x *= 1.1
    i += 1
print(f"Num of day = {i}")

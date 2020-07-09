# Task4
num2 = 0
num = int(input("Please, input very very big number: "))
while num !=0:
    if num2 < (num % 10):
        num2 = num % 10
    num //= 10
print(f"Biggest number in a very very big number = {num2}")


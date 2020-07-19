import random

list1 = []
for i in range(10):
    list1.append(random.randrange(10))
print(list1)
print([a for a in list1 if list1.count(a) == 1])
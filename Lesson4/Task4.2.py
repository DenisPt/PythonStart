import random

list1 = [i for i in range(20)]
random.shuffle(list1)

list2 = [list1[i] for i in range(1, len(list1)) if list1[i] > list1[i-1]]
print(list2)
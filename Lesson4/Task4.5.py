from functools import reduce

print(reduce(lambda s, x: s * x, range(100, 1001, 2)))
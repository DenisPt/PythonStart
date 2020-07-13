bigList = [1, 1.0, "1", True, [0, 1], (0,1), {0, 1}, {0: "0", 1: "1", "0": 0, "1": 1}]
for c in bigList:
    print(f"type of {c} = {type(c)}")
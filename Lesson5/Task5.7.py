import json
dic = {}
with open("Task5.7.txt", "r", encoding="utf-8") as file1:
    while True:
        content = file1.readline()
        content = content.split()
        if content == []:
            break
        dic.update([[content[0], int(content[2]) - int(content[3])]])
        print(dic)
li = [dic, {"average_profit": round(sum([c for c in dic.values() if c > 0]) / len([c for c in dic.values() if c > 0]))}]
with open("Task5.7(result).json", "w", encoding="utf-8") as file1:
    json.dump(li, file1, ensure_ascii=False)
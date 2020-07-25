import re
with open("Task5.6.txt", "r", encoding="utf-8") as file1:
    content = file1.readlines()
print(content)
dic ={}
for string in content:
    object = re.findall(r'(\w*?):', string)
    time = re.findall(r'(\d+)', string)
    dic.update([[object[0], sum(map(int, time))]])
print(dic)

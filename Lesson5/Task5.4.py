from googletrans import Translator
trans = Translator()
with open("Task5.4.txt", "r", encoding="utf-8") as file1:
    text1 = file1.read()
text1 = trans.translate(text1, src="en", dest="ru")
with open("Task5.4(result).txt", "w", encoding="utf-8") as file1:
    print(text1.text, file=file1)

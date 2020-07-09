# Task2
sec = int(input("Input few seconds: "))
print(f"{sec // (60 * 60):02d}:{(sec % (60 * 60)) // 60:02d}:{sec % 60:02d}")

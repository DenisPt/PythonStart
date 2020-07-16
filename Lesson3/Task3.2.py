def pr(**kwargs):
    return kwargs.values()


for w in pr(name=input("Введите имя: "),
            family=input("Введите фамилию: "),
            birth=input("Введите год рождения: "),
            city=input("Введите город проживания: "),
            email=input("Введите email: "),
            phone=input("Введите телефон: ")):
    print(w, end=" ")

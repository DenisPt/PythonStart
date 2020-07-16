def capitalize2(word):
    s = list(word)
    try:
        s[0] = chr(ord(s[0]) - 32)
    except IndexError:
        pass
    return ''.join(s)

str = input("Введите строку в маленьком регистре латинского алфавита: ").split(" ")
alph = range(ord("a"), ord("z")+1)
err = False
while True:
    for word in str:
        for ch in word:
             if ord(ch) not in alph:
                   err = True
    if err:
        print("Введен неверный формат строки")
        break
    """Первый способ"""
    for word in str:
        print((lambda word: word.title())(word), end=" ")

    print()

    """Второй способ"""
    for word in str:
        print(capitalize2(word), end=" ")
    break

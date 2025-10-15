a = 10
b = 10


def dodaj():
    a = 7  # zmienna lokalna,
    b = 8  # nie zmienia wartości zmiennej globalnej o tej samej nazwie
    print(a + b)


def dodaj2():
    print(a + b)  # przyjmie wartości globalne


def dodaj3():
    global a  # użyj wewnatrz funkcji globelnej zmiennej a
    a = 9  # zmieni wartość zmiennej globalnej a
    b = 17
    print(a + b)


print(f"Wartość a z góry (globalny) {a}")  # Wartość a z góry (globalny) 10
dodaj()  # 15
print(f"Wartość a z góry (globalny) {a}")  # Wartość a z góry (globalny) 10
dodaj2()  # 20
print(f"Wartość a z góry (globalny) {a}")  # Wartość a z góry (globalny) 10
dodaj3()  # 26
print(f"Wartość a z góry (globalny) {a}")  # Wartość a z góry (globalny) 9
dodaj2()  # 19

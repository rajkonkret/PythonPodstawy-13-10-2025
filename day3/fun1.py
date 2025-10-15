# funkcje - wydzielony fragment kodu, można wywołać w dowolnym momencie
# funkcja musi byc najpierw zadeklarowana
# żeby uruchomić funkcję, musi zostać wywołana

a = 8
b = 9


# funkcje nie zwracają wyniku
# deklaracja funkcji
def dodaj():
    print(a + b)


def dodaj2(a, b):
    print(a + b)


# argument c o wartości domyslnej
# zasymulowanie przeciążania funkcji liczbą argumentów
def odejmij(a, b, c=0):
    print(a - b - c)


# przekazywanie argumentów po pozycji
# wywołanie funkcji
dodaj()  # 17

# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(5, 9)  # 14

odejmij(1, 2, 3)  # -4
odejmij(1, 2)  # -1 c=0

# przekazanie argumentów po nazwie
odejmij(b=7, c=9, a=10)  # -6
odejmij(b=89, a=90)  # 1

# mieszane
odejmij(1, 2, c=90)  # -91
odejmij(1, b=9, c=90)  # -98

# argumenty pozycyjne muszą byc przed nazwanymi
# odejmij(a=10, 1, 3) # SyntaxError: positional argument follows keyword argument

# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# print(dodaj() + dodaj2(3, 9))
print(dodaj())  # None

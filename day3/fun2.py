# funkcje zwracające wynik
def dodaj(a, b):
    return a + b  # zwraca wynik


def odejmij(a=0, b=0, c=0):
    return a - b - c


print(dodaj(4, 8))  # 12
zm = dodaj(4, 6)
print("Wynik:", zm)  # Wynik: 10

print(odejmij(1, 2, 3))  # -4
print(odejmij(1, 2))  # -1
print(odejmij(1, b=2))  # -1

print(dodaj(5, 7) + dodaj(6, 90))  # 108

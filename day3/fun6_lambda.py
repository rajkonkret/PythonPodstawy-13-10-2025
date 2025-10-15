# funkcja lambda
# skrócony zapis funkcji
# return - zwraca wynik

def odejmij(a, b):
    return a - b


print(odejmij(3, 1))  # 2

# labda zawsze zwraca wynik (return)
odejmij2 = lambda a, b: a - b
print(odejmij2(10, 7))  # 3

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(10))  # nastolatek
print(wiek(18))  # dorosły

# mapowanie danych
lista = [1, 2, 3, 4, 35, 55, 60, 100, 500]
l1 = []
for i in lista:
    l1.append(i * 2)
print(l1)  # [2, 4, 6, 8, 70, 110, 120, 200, 1000]

print([i * 2 for i in lista])


# [2, 4, 6, 8, 70, 110, 120, 200, 1000]

def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)  # [2, 4, 6, 8, 70, 110, 120, 200, 1000]

# map() - dla wszystkich eleemntów kolekcji wykonuje zadaną funkcję
# funkcja wyzszego rzędu - przyjmuje inną funkcje jako argument

# podajemy adres funkcji
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 70, 110, 120, 200, 1000]

# funkcja anonimowa - nie jest przypisana do jakiejkolwiek zmiennej
# deklaracja w miejscu użycia
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 70, 110, 120, 200, 1000]
print(f"Zastosowanie map(): {list(map(lambda x: x * 3, lista))}")
# Zastosowanie map(): [3, 6, 9, 12, 105, 165, 180, 300, 1500]
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
# Zastosowanie map(): [4, 8, 12, 16, 140, 220, 240, 400, 2000]

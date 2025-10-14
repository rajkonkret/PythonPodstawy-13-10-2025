# pętla - mozliwość wykonania tego samego kodu
# for - iteracyjna
import random

for i in range(5):  # od 0 do 4
    print(i)
# 0
# 1
# 2
# 3
# 4

for i in range(6):
    pass  # nic nie rób

for _ in range(3):
    print("Test podłoga")
    print(_)
# Test podłoga
# 2

for i in range(10):
    print(i * 2)
    print(i + 2)

# przerobic zadanie lotto na petle
lista_kula = list(range(1, 50))  # od 1 do 49
lista_wynik = []

for _ in range(6):
    wyn = random.choice(lista_kula)
    lista_kula.remove(wyn)
    print(wyn)
    lista_wynik.append(wyn)

print(lista_wynik)  # [18, 22, 39, 47, 11, 1]

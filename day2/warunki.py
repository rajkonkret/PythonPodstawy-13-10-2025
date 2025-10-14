# instrukcje warunkowe
# instrukcje strowanie przepływem programu
# w zależnoci od warunku (True/False) wykona odpowiedni blok programu

odp = True
# debugger
# ustawiamy pułapki
odp = False
if odp:  # bool(odp)
    # Blok wykonany tylko gdy True
    print("Nowy blok programu po if")
    print("Nowy blok programu po if")
    print("Nowy blok programu po if")
    print("Nowy blok programu po if")
    print("Nowy blok programu po if")

print('Niezależna od if')

odp = "Radek"
print(bool(odp))
if odp:
    print("Radek")
    # Radek

if odp == "Radek":  # == porównanie
    print("Radek")
# Radek

odp = 0
if odp:
    print("Działa")
else:  # w przeciwnym wypadku, domyslna
    print("Zero -> False")
# Zero -> False

a = "Radek"
# warunek ma sie wykonac, gdy długosć większa niż 3
if len(a):
    print(f"Długość wynosi: {len(a)}")
# Długość wynosi: 5

a = "Radek"
n = len(a)
if n:
    print(f"Długość wynosi: {n}")
# Długość wynosi: 5

# walrus operator, operator morsa
if (n := len(a)) > 3:
    print(f"Długość wynosi: {n}")
# Długość wynosi: 5

podatek = 0
zarobki = int(input("Podaj zarobki:"))

# kolejność ma znaczenie
if zarobki < 10_000:
    podatek = 0
elif zarobki < 40_000:
    podatek = 0.2
elif zarobki < 100_000:
    podatek = 0.4

else:
    podatek = 0.9

print(f"Podatek wynosi: {podatek * zarobki} pln.")
# Podaj zarobki:5000
# Podatek wynosi: 0 pln.
# Podaj zarobki:50000
# Podatek wynosi: 20000.0 pln.
# 0.2 dla przedziału od 10000 do 39999
# Podaj zarobki:25000
# Podatek wynosi: 5000.0 pln.

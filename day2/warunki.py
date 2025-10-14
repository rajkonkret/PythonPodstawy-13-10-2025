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

# podatek = 0
# zarobki = int(input("Podaj zarobki:"))
#
# # kolejność ma znaczenie
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
#
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi: {podatek * zarobki} pln.")
# Podaj zarobki:5000
# Podatek wynosi: 0 pln.
# Podaj zarobki:50000
# Podatek wynosi: 20000.0 pln.
# 0.2 dla przedziału od 10000 do 39999
# Podaj zarobki:25000
# Podatek wynosi: 5000.0 pln.

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0

print("Rabat wynosi:", rabat)
# Rabat wynosi: 25
rabat = 25 if suma_zam > 100 else 0  # operator warunkowy
print("Rabat wynosi:", rabat)  # Rabat wynosi: 25

# napisac test z...
# dodac punktację
# punkty = 0
# odp = input("Podaj date Chrztu Polski")  # -> str
# if odp == '966':
#     print("dobrze")
#     # punkty = punkty + 1
#     punkty += 1
# else:
#     print("Musisz jescze sie douczyć")
# # Podaj date Chrztu Polski966
# # dobrze
# print("Punkty:", punkty)
# # dobrze
# # Punkty: 1
# odp = input("Podaj dateBitwy pod Grunwaldem")  # -> str
# if odp == '1410':
#     print("dobrze")
#     # punkty = punkty + 1
#     punkty += 1
# else:
#     print("Musisz jescze sie douczyć")
# print("Punkty:", punkty)

alert_system = "console"
lista_b = []
error_level = "error"

if alert_system == "console":
    print("Stało się cos strasznego")
elif alert_system == "email":
    print("System email")
    if error_level == "error":
        lista_b.append("Krytyczny")
else:
    print("Inny")

print(lista_b)

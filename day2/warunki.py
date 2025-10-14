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

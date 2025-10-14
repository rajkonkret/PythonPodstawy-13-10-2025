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


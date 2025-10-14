# while - sterowana warunkiem

# petla nieskończona
# while True:
#     print("Komunikat 1")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerywa bieżące działanie petli
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!

print(licznik)  # 11

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")

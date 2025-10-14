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

# password = input("Podaj hasło")
# while password != "secret":
#     password = input("Błędne hasło, Podaj ponownie")
# print("Hasło prawidłowe")
# Podaj hasłoaaa
# Błędne hasło, Podaj ponownieaaaa
# Błędne hasło, Podaj ponownieaaaa
# Błędne hasło, Podaj ponownieaaaaa
# Błędne hasło, Podaj ponowniesssss
# Błędne hasło, Podaj ponowniesecret
# Hasło prawidłowe

lista = []
lista_int = []
while True:
    #  A string is numeric if all characters in the string are numeric
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)
print(lista_int)  # [1, 2, 3, 4, 5]
# Podaj liczbę1
# Podaj liczbę2
# Podaj liczbę3
# Podaj liczbę4
# Podaj liczbę5
# Podaj liczbęa
# ['1', '2', '3', '4', '5']

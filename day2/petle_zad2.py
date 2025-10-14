dane = {"imie": "Radek", 'nazwisko': "Kowalski"}
print(type(dane))  # <class 'dict'>

# wypisze klucze
for i in dane:
    print(i)
# imie
# nazwisko

for k in dane.keys():
    print(k)
# imie
# nazwisko

# wypisanie wartości
for v in dane.values():
    print(v)
# Radek
# Kowalski

# wypisanie par
for i in dane.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dane.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
# sep
#         string inserted between values, default a space.

for k, v in dane.items():
    print(k, v, sep="<+++>")
# imie<+++>Radek
# nazwisko<+++>Kowalski

# end
#         string appended after the last value, default a newline.
for k, v in dane.items():
    print(k, v, end="")
# imie Radeknazwisko Kowalski - nie przeszło do nowej linii

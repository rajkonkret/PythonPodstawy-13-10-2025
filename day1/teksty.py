tekst = "Witaj"

print(tekst)
print(type(tekst))
# Witaj
# <class 'str'>

# teksty sa niemutowalne
tekst.upper()
print(tekst)
""" Return a copy of the string converted to uppercase. """
print(tekst.upper())  # WITAJ
upper_case = tekst.upper()
print(upper_case)  # WITAJ

tekst = "Witaj Świecie"

print(tekst.capitalize())  # Witaj świecie
print(tekst.lower())  # witaj świecie

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usunięcie białych znaków
print(tekst.removeprefix("Witaj").strip())  # "Świecie"

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9awiecie'
print(type(encoded_s))  # <class 'bytes'>, typ bajtowy
print(encoded_s.decode("utf-8"))  # Witaj Świecie

print(tekst)
# Witaj Świecie
# 0123456789....

print(tekst[4])  # "j" indeks 4

print(tekst.count("i"))  # 3 występuje 3 razy
print(tekst.count("j", 0, 4))  # wystepuje 0 razy, indeksy 0123, z prawej zbiór otwarty



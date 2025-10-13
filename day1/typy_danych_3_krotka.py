# krotka, tupla - tylko do odczytu, niemutowalna kolekcja
# pozwala efektywniej zarządzać pamięcią
# stała - zmienna

tupla_imiona = ("Radek", "Tomek", "Zenek", "Roman")
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Roman')
print(type(tupla_imiona))  # <class 'tuple'>

tupla_liczby = 43, 55, 22.34, 11, 200
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>

tupla = 43,
print(tupla)  # (43,)
print(type(tupla))  # <class 'tuple'>

# PEP8 zaleca by jednoeleemntową tuplę robić z nawiasami
tupla2 = (43,)
print(tupla2)  # (43,)
print(type(tupla2))  # <class 'tuple'>

# tupla_liczby[3] = 123  # TypeError: 'tuple' object does not support item assignment
del tupla_liczby  # skasowanie całej tupli
# print(tupla_liczby)  # NameError: name 'tupla_liczby' is not defined

print(tupla_imiona.index("Radek"))  # index 0
print(tupla_imiona.count("Radek"))  # występuje 1 raz

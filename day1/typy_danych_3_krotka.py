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

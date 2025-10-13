# zbiór (set) - przechowują unikalne wartości
# nie zachowują kolejności przy dodawania elementów
# nie mają indexu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(type(zbior))  # <class 'set'>
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

# pusty zbiór
zb2 = set()  # pusty zbiór tworzymy za pomoca słówka set()
print(zb2)  # set() - pusty zbiór
print(type(zb2))  # <class 'set'>

# dodanie elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(18)
zbior.add(33)
zbior.add(24)
zbior.add(32)
zbior.add(17)
print(zbior)
# {32, 33, 66, 777, 11, 44, 17, 18, 22, 55, 24}

# usunięcie elemntu ze zbioru
zbior.remove(55)
print(zbior)  # {32, 33, 66, 777, 11, 44, 17, 18, 22, 24}

# pop() - usunięcie pierwszego elementu
print(zbior.pop())  # 32
print(zbior)  # {33, 66, 777, 11, 44, 17, 18, 22, 24}

print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 17, 18, 22, 24}

zmienna = zbior.pop()
print("Usunięty:", zmienna)  # Usunięty: 66

# operacje na zbiorach
zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}
print(type(zbior_2))  # <class 'set'>
print(zbior_2)  # {18, 667, 52, 11, 44, 12.34, 62}

# suma zbiorów - zwraca nowy zbiór
print(zbior | zbior_2)  # {777, 11, 44, 12.34, 17, 18, 52, 22, 24, 667, 62}
print(zbior.union(zbior_2))  # {777, 11, 44, 12.34, 17, 18, 52, 22, 24, 667, 62}
print(zbior)  # {777, 11, 44, 17, 18, 22, 24}
print(zbior_2)  # {18, 667, 52, 11, 44, 12.34, 62}

zbior_3 = {18, 667, 52, 11, 44, 12.34, 62, 99, 88}
print(zbior_3)  # {99, 11, 44, 12.34, 18, 52, 88, 667, 62}
print(zbior.union(zbior_2, zbior_3))
# {777, 11, 12.34, 17, 18, 22, 24, 88, 667, 99, 44, 52, 62}

# część wspólna - zwraca nowy zbiór
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica zbiorów
print(zbior - zbior_2)  # {24, 777, 17, 22}
# {777, 11, 44, 17, 18, 22, 24} - {18, 667, 52, 11, 44, 12.34, 62} = {24, 777, 17, 22}

print(zbior.difference(zbior_2))  # {24, 777, 17, 22}
print(zbior_2.difference(zbior))  # {667, 52, 12.34, 62}

# update() - łączy zbiory, zapisuje w zbiorze
# nadpisuje bazowy zbiór
print(zbior)  # {777, 11, 44, 17, 18, 22, 24}
zbior.update(zbior_2)
print(zbior)  # {777, 11, 44, 12.34, 17, 18, 52, 22, 24, 667, 62}

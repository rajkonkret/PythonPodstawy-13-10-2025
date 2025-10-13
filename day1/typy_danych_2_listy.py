# kolekcje

# lista - przechowuje dowolną ilosć eleemntów, dowolnego typu na raz
# zachowuje kolejność przy dodawaniu elementów

# tworzenie pustej listy
lista = []
print(lista)
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodanie elementów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Oliwier")
lista.append("Anna")
lista.append("Aga")
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Oliwier', 'Anna', 'Aga']
#     0        1        2         3         4      5

print(lista[1])  # Tomek
print(lista[3])  # Oliwier

# print(lista[10])  # IndexError: list index out of range

print(len(lista))  # 6
print(lista[len(lista) - 1])  # Aga
print(lista[-1])  # Aga, ostatni elemnt z listy
# ['Radek', 'Tomek', 'Zenek', 'Oliwier', 'Anna', 'Aga']
#     0        1        2         3         4      5
#     -6       -5       -4        -3        -2     -1

print(lista[-2])  # Anna

# fragment z listy - slicowanie
print(lista[0:3])  # 012, ['Radek', 'Tomek', 'Zenek']
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']
print(lista[2:])  # ['Zenek', 'Oliwier', 'Anna', 'Aga'] - z ostatnim włącznie
print(lista[2:5])  # ['Zenek', 'Oliwier', 'Anna']

print(lista[2:15])  # ['Zenek', 'Oliwier', 'Anna', 'Aga']
print(lista[20:234])  # [] - pusta lista

print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Oliwier', 'Anna', 'Aga']

print(lista[2:2])  # []
print(lista[2:3])  # ['Zenek']

print(lista[::2])  # [start:stop:krok], ['Radek', 'Zenek', 'Anna'], co drugi

# ['Radek', 'Tomek', 'Zenek', 'Oliwier', 'Anna', 'Aga']
#     0        1        2         3         4      5
#     -6       -5       -4        -3        -2     -1
print(lista[-2:0])  # [], [4:0]
print(lista[0:-2])  # [0:4] # ['Radek', 'Tomek', 'Zenek', 'Oliwier']

lista_15 = list(range(15))  # int od 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[::2])  # [0, 2, 4, 6, 8, 10, 12, 14]

print(lista_15[::-1])  # [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(lista_15[::-3])  # [14, 11, 8, 5, 2]

# nadpisanie elemntu
lista[3] = "Radek"
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Radek', 'Anna', 'Aga']

# dopisanie eleemntu do listy na wskazanym indeksie
lista.insert(1, "Roman")
print(lista)
# ['Radek', 'Roman', 'Tomek', 'Zenek', 'Radek', 'Anna', 'Aga']
print(len(lista))  # nowa długosc listy: 7

# sprawdzenie numeru indeksu dla elementu, pierwszy od lewej
print(lista.index("Radek"))  # 0

print(lista.count("Radek"))  # element występuje 2 razy

# usunięcie elementu, pierwszy z lewej
lista.remove("Radek")
print(lista)
# ['Roman', 'Tomek', 'Zenek', 'Radek', 'Anna', 'Aga']

# usunięcie po indeksie, zwraca co usunął
print(lista.pop(4))  # Anna
print(lista)  # ['Roman', 'Tomek', 'Zenek', 'Radek', 'Aga']
print(lista.pop())  # Aga, usunie ostatni element

a = 1
b = 3
a = b
print(a, b)  # 3 3
b = 9
print(a, b)  # 3 9

lista2 = lista  # kopia referencji, adresu
print(lista2)
print(lista)
lista_copy = lista.copy()  # kopia elemntów listy
# ['Roman', 'Tomek', 'Zenek', 'Radek']
# ['Roman', 'Tomek', 'Zenek', 'Radek']
lista.clear()  # usunięcie wszystkich elemetów z listy
print(lista2)  # []
print(lista)  # []
print(lista_copy)  # ['Roman', 'Tomek', 'Zenek', 'Radek']
print(id(lista))
print(id(lista2))
print(id(lista_copy))
# 1416163151808
# 1416163151808
# 1416165021376

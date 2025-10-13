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

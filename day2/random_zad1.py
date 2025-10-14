import random

# operacje na liczbach pseudolosowych

"""Return random integer in range [a, b], including both end points.
        """
print(random.randint(1, 100))  # int, 6, od 1 do 100

print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5))  # int od 0 do 4

print(random.random())  # 0.8135530132734263, od 0 do 0.999999
print(random.random() * 10)  # 5.288950225995749, od 0 do 9.999999

lista = [67, 45, 22, 68, 69, 90, 42]
print(lista)  # [67, 45, 22, 68, 69, 90, 42]
print(random.randrange(len(lista)))  # 4 wylosowany indeks
print(random.choice(lista))  # wylosowanie elementu listy, 90

lista_kula = list(range(1, 50))  # od 1 do 49
# print(lista_kula)

wyn = random.choice(lista_kula)
lista_kula.remove(wyn)
print(wyn)

print(random.choices(lista_kula, k=6))  # [20, 13, 1, 1, 47, 39] z powtórzeniami
print(random.sample(lista_kula, k=6))  # [32, 31, 47, 6, 49, 25], bez powtórzeń
print(random.sample(lista_kula, 6))  # [12, 34, 11, 49, 24, 35], bez powtórzeń

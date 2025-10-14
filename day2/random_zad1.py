import random

# operacje na liczbach pseudolosowych

"""Return random integer in range [a, b], including both end points.
        """
print(random.randint(1, 100))  # int, 6, od 1 do 100

print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5))  # int od 0 do 4

print(random.random())  # 0.8135530132734263, od 0 do 0.999999
print(random.random() * 10)  # 5.288950225995749, od 0 do 9.999999

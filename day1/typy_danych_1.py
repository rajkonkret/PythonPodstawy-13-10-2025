wiek = 47  # int
rok = 2025
temp = 36.3  # float

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # 0.023209876543209877 -> float
print(4 / 2)  # 2.0

print(rok // wiek)  # 43, część całkowita z dzielenia
print(rok % wiek)  # modulo, reszta z dzielenia, 4
print(10 % 3)  # reszta 1

print(wiek ** rok)  # potegowanie

# len() - długość
print(len(str(wiek ** rok)))  # 3386 długość
# print(len(str(wiek ** rok ** 2))) #
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 4 / 1 + 4 / 2)  # 36.0
print(54 - (5 * 4 / 1 + 4) / 2)  # 42.0

# float
# bład zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# For example, in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal() - obejscie problemu zaokrąglenia

# typ logiczny
# prawda, fałsz
# True, False
# 1, 0
czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'>, typ logiczny, boolean

print(int(True))  # 1
print(int(False))  # 0

# bool() - rzutowanie na typ logiczny
print(bool(1))  # True
print(bool(0))  # False

print(bool(100))  # True
print(bool(-100))  # True
print(bool("Radek"))  # True

print(bool(""))  # False
print(bool(None))  # False, nic, nie wiem, stan nieokreślony, odpowiednik null

# and - i
print(True and False)  # False
print(True and True)  # True

# or - lub
print(True or False)  # True
print(True or True)  # True
print(False or False)  # False

# not - negacja
print(not True)  # False
print(not False)  # True

a = 7
b = 89

print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 7 > 89 = False
print(f"Porównanie {a} < {b} = {a < b}")  # Porównanie 7 < 89 = True
print(f"Porównanie {a} <= {b} = {a <= b}")  # Porównanie 7 <= 89 = True
print(f"Porównanie {a} >= {b} = {a >= b}")  # Porównanie 7 >= 89 = False
print(f"Porównanie {a} != {b} = {a != b}")  # Porównanie 7 != 89 = True,  czy różne
print(f"Porównanie {a} == {b} = {a == b}")  # Porównanie 7 == 89 = False, czy równe

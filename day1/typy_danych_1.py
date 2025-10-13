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

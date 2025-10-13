user = "Tomek"  # str
wiek = 67  # int
wersja = 3.900001
print(type(wersja))  # <class 'float'>, liczby zmiennoprzecinkowe
liczba = 890123456987123  # int

print("Witaj %s, masz teraz %d lat" % (user, wiek))
# Witaj Tomek, masz teraz 67 lat
# %s - str
# %d - digit

# sprawdza typy danych
# print("Witaj %d, masz teraz %s lat" % (user, wiek))
# TypeError: %d format: a real number is required, not str

print(f"Witaj {user}, masz teraz {wiek} lat.")
# Witaj Tomek, masz teraz 67 lat.

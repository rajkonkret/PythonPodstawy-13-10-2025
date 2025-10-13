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

print("Uzywamy wersji pythona %i" % 3)  # Uzywamy wersji pythona 3
print("Uzywamy wersji pythona %f" % 3)  # Uzywamy wersji pythona 3.000000
# %f - float
print("Uzywamy wersji pythona %f" % 3.9)  # Uzywamy wersji pythona 3.900000
print("Uzywamy wersji pythona %.2f" % 3.9)  # Uzywamy wersji pythona 3.90
print("Uzywamy wersji pythona %.1f" % 3.9)  # Uzywamy wersji pythona 3.9
print("Uzywamy wersji pythona %.0f" % 3.9)  # Uzywamy wersji pythona 4 - zaokrągla
print("Uzywamy wersji pythona %.f" % 3.9)  # Uzywamy wersji pythona 4 - zaokrągla

print(f"Używamy wersji pythona {wersja}")  # Używamy wersji pythona 3.900001
print(f"Używamy wersji pythona {wersja:.1f}")  # Używamy wersji pythona 3.9
print(f"Używamy wersji pythona {wersja:.2f}")  # Używamy wersji pythona 3.90
print(f"Używamy wersji pythona {wersja:.0f}")  # Używamy wersji pythona 4

user = "Tomek"
print(f"{user:>10}")  # "     Tomek" do prawej
print(f"{user:<20}")  # "Tomek               " do lewej
print(f"{user:^20}")  # "       Tomek        " centrowanie

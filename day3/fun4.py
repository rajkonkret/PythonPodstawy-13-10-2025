# stworzyc funkcje obliczającą średnią


def srednia(name=None, *cyfry):  # dowolna ilosć argumentów pozycyjnych
    print(cyfry)
    count = len(cyfry)
    suma_p = sum(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
        avg_p = suma_p / count
    except Exception as e:
        print("Błąd:", e)
    else:  # wykona się tylko gdy nie ma błedu
        print(f"Średnia dla ucznia {name}, wynosi: {avg}")
        print(f"Średnia dla ucznia {name}, wynosi: {avg_p}")
    finally:
        print("Kolejny uczeń")


srednia()  # ()
srednia(1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5)
srednia("Radek", 5, 6, 5, 6, 5)
# ()
# Błąd: division by zero
# Kolejny uczeń
# (2, 3, 4, 5)
# Średnia dla ucznia 1, wynosi: 3.5
# Średnia dla ucznia 1, wynosi: 3.5
# Kolejny uczeń
# (5, 6, 5, 6, 5)
# Średnia dla ucznia Radek, wynosi: 5.4
# Średnia dla ucznia Radek, wynosi: 5.4
# Kolejny uczeń

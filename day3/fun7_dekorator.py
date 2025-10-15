# funkcja dekorator
# dodają funkcjonalność do istniejących funkcji
def dekorator(func):
    def wrapper():
        print("Dekorujemy!!!")
        return func()

    return wrapper  # zwracamy adres funkcji


@dekorator
def hello():
    print("Witaj Świecie")


hello()  # Witaj Świecie
# po użyciu dekoratora
# Dekorujemy!!!
# Witaj Świecie

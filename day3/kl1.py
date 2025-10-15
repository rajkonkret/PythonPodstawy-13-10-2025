# programowanie obiektowe
# klasa - szablon, przepis, opis
# obiekt - instancja klasy - stworzone wg przepisu
# klasa musi byc zadeklarowana przed użycia
# tworzenie obiektu wywołuje metodę inicjalizującą (konstruktor)
# paradygmaty programowania obiektowego
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

# PEP8 zaleca nazwy klas PascalCase
class Human:
    """
    Klasa Human w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"


print(Human.__doc__)  # Klasa Human w Pythonie - dokumentacja

# tworzenie obiektu klasy
cz1 = Human()
print(cz1)  # <__main__.Human object at 0x000001EDA84181A0>
print(cz1.plec)  # k
print(cz1.imie)  #
print(cz1.wiek)  # None

cz1.imie = "Radek"
cz1.wiek = 56
cz1.plec = "m"
print(cz1.plec)  # m
print(cz1.imie)  # Radek
print(cz1.wiek)  # 56

cz2 = Human()
cz2.imie = "Anna"
cz2.wiek = 38
print(cz2.plec)  # k
print(cz2.imie)  # Anna
print(cz2.wiek)  # 38

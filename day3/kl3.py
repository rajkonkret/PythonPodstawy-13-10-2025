from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa Ptak w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # metoda abstarkcyjna
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """
    Klasa dziedziczy po klasie Ptak
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # obowiązkowo musimy wywołać konstruktor z klasy wyższej

    def latam(self):
        print("Tu", self.gatunek, 'Ja nie latam.')

    def wydaj_odglos(self):
        print("Ko ko ko ko")

    def dziobanie(self):
        print("Dziobanie")


class Orzel(Ptak):
    """
    Dziedziczy po Ptak
    """

    def wydaj_odglos(self):
        print("kier kir kier")

    def polowanie(self):
        print("Rozpoczynam polowanie")


# nie mozna stworzyc obiektów klasy Ptak
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzeł", 50)
# or1.latam()  # Tu Orzeł Lecę z szybkością 50
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura 2")
kur2.latam()  # Tu Kura 2 Ja nie latam.
kur2.wydaj_odglos()  # Ko ko ko ko

or2 = Orzel("Orzel Bielik", 55)
or2.latam()
or2.wydaj_odglos()
# Tu Orzel Bielik Lecę z szybkością 55
# kier kir kier

# polimorfizm - obiekty róznych klas mają wspolne cechy wymuszene poprzez klase abstrakcyjną
lista = [or2, kur2]
for i in lista:
    i.wydaj_odglos()
# kier kir kier
# Ko ko ko ko

kur2.dziobanie()
or2.polowanie()
# Dziobanie
# Rozpoczynam polowanie
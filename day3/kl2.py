class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    # self - obiekt wywołujący metodę
    def powitanie(self):
        print(f"Nazywam się: {self.imie}")


# TypeError: Human.__init__() missing 2 required positional arguments: 'imie' and 'wiek'
# cz1 = Human()
cz1 = Human("Radek", 67, "m")
print(cz1.wiek)
print(cz1.imie)
print(cz1.plec)
# 67
# Radek
# m
cz1.powitanie()
# Nazywam się: Radek

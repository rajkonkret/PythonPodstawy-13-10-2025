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

    def ruszaj(self):
        if self.plec == "m":
            print("Ruszyłem w drogę")
        else:
            print("Ruszyłam w drogę")


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

cz2 = Human("Anna", 65)
print(cz2.imie)  # Anna
print(cz2.wiek)  # 65
print(cz2.plec)  # k

cz2.powitanie()  # Nazywam się: Anna

cz1.ruszaj()  # Ruszyłem w drogę
cz2.ruszaj()  # Ruszyłam w drogę

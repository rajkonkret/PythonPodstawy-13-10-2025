# funkcja lambda
# skrócony zapis funkcji
# return - zwraca wynik

def odejmij(a, b):
    return a - b


print(odejmij(3, 1))  # 2

# labda zawsze zwraca wynik (return)
odejmij2 = lambda a, b: a - b
print(odejmij2(10, 7))  # 3

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(10))  # nastolatek
print(wiek(18))  # dorosły

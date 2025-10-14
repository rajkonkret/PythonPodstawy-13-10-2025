# słownik - para klucz - wartosć
# klucze nie mogą się powtarzać
# {'user':'Radek'}
# odpowiednik jsona

# pusty słownik
dictionary = {}
print(type(dictionary))  # <class 'dict'>
print(dictionary)  # {}

pusty_dict = dict()
print(pusty_dict)  # {}
print(type(pusty_dict))  # <class 'dict'>

# dodani elementu do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 50
print(dictionary)  # {'imie': 'Radek', 'wiek': 50}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 50])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 50)])

dict_list = {"imie": ["Radek", "Tomek", "Zenek"]}
print(dict_list)  # {'imie': ['Radek', 'Tomek', 'Zenek']}

# wypisanie wartości ze słownika
print(dictionary['imie'])  # Radek

print(dict_list['imie'])  # ['Radek', 'Tomek', 'Zenek']
print(dict_list['imie'][0])  # Radek
print(dict_list['imie'][1])  # Tomek

# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary.get('Imie'))  # None
print(dictionary.get('imie'))  # Radek
# możemy określic wartosc domyslną
print(dictionary.get('Imie', "default"))  # default

dictionary.update({"data": "31-12-2030"})
print(dictionary)
# {'imie': 'Radek', 'wiek': 50, 'data': '31-12-2030'}

dict_small = {"x": 4}
print(dict_small)  # {'x': 4}
dict_small.update([("a", 8), ("c", 8)])
print(dict_small)  # {'x': 4, 'a': 8, 'c': 8}

# input() - wprowadzanie danych np.:  z klawiatury
# tekst = input("Podaj imię:")
# print(tekst)
# Podaj imię:Radek
# Radek
# napisac aplikacje kalkulator
# pobrac dane 2x input()
# # wyswietlic wynik obliczenia (+) print()
# a = int(input("Podaj pierwszą liczbę:"))  # input zwraca str()
# b = float(input("Podaj drugą liczbę:"))
# # print(a + b) # konkatenacja
# print(int(a) + int(b))

# napisać program słownik pol-ang
pol_ang = {"kot": "cat", "pies": "dog", "dach": "roof"}
print(f"znam słowa: {pol_ang.keys()}")
odp = input("Podaj słowo do przetłumaczenia:")
# print(f"Tłumaczenie słowa {odp}: {pol_ang[odp.strip().lower()]}")
print(f"Tłumaczenie słowa {odp}: {pol_ang.get(odp.strip().lower(), "Nie ma")}")

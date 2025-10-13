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

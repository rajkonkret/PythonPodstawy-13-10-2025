# https://peps.python.org/pep-0008/
# ctrl alt l - formatowanie kodu
import sys

print()  # wypisz/wydrukuj
print("Radek")
print('Radek')
# Radek
# Radek

# ctrl / - komentarz
# print('Radek") - linijka z błędem
#   File "C:\Users\Szkolenie\PycharmProjects\PythonPodstawy-13-10-2025\day1\pierwszy.py", line 9
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 9)
#
# Process finished with exit code 1 - program z błędem
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
# ctrl d - powielanie linii

# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>, string, tekstowe

print("39")
print(type("39"))  # <class 'str'>
print("39" + "39")  # 3939, łączenie tekstów, konkatenacja

print(39)
print(type(39))  # <class 'int'>, liczba całkowita
print(39 + 39)  # 78

# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str

# rzutowanie typów - zamiana na inny typ
print(int("39") + 39)  # 78 int() - rzutowanie na inta

print("Radek" + str(1))  # Radek1, str() - rzutowanie na str

print(168 * "35")
print(4 * "*")  # ****
print(168 * 35)  # 5880
print(int(168) + int(35))  # 203

print(50 * "-")
# --------------------------------------------------
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300,
# str_digits_check_threshold=640)

# zmienna - pudełko na dane
# snake_case
# zmienna ma podpowiadac co przechowuje

# typowanie dynamiczne - typ na podstawie danych
# w każdej chwili można wrzucic dane innego typu
name = "Radek"
print(name)  # Radek
print(type(name))  # <class 'str'>

name = 90
print(name)
print(type(name))

# podpowiedzi typów
name: str = "Radek"
print(name)
print(type(name))  # <class 'str'>

name = 90
print(name)
print(type(name))  # <class 'int'>

age = 90
print(age)  # 90

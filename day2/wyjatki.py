# wyjątek - bład podczas wykonywania programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\Szkolenie\PycharmProjects\PythonPodstawy-13-10-2025\day2\wyjatki.py", line 1, in <module>
#     print(5/0)
#           ~^~
# ZeroDivisionError: division by zero

try:
    # print(5 / 0)
    # print("a" * "23")
    # print(int("a"))
    # raise KeyError("Brak klucza")  # rzucamy jawnie błędem
    value = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Błąd typu")
except ValueError:
    print("Błąd wartości")
except Exception as e:
    print("Bład:", e)
else:  # wykona się tylko gdy nie ma błedu
    print("Wartośc:", value)
finally:  # wykona się zawsze
    print("Wykona się zawsze")
print("Dalsza częśc programu")
# Nie dziel przez zero
# Dalsza częśc programu
# Błąd typu
# Dalsza częśc programu
# Bład: 'Brak klucza'
# Dalsza częśc programu
# Wartośc: 30.0
# Wykona się zawsze
# Dalsza częśc programu
